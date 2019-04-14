import requests
from bs4 import BeautifulSoup as bs
import shutil
import os


# Settings
PROVIDER = 'http://www.mangareader.net/'
LOCAL_PATH = '/home/Manga/'
INITIAL_PAGE = 1
ESTIMATED_MAX_DIGITS = 3
FILE_EXT = '.jpg'


# sending a request
def send_request(url, binary=False):
    try:
        request = requests.get(url, stream=binary)
    except:
        print('There was an error.')
        exit()

    return request


# checking to see if the chapter was released
def released_or_not(mangaTitle, chapterNum):
    manga_url = get_page_url(mangaTitle, chapterNum)
    html = send_request(manga_url).text

    return 'not released' in html


# adding zeros to the page numbers
def add_zeros(pageNum):
    digits = len(pageNum)
    zeros = '0' * (ESTIMATED_MAX_DIGITS - digits)
    return zeros + pageNum


# converting the manga name
def nameChanger(title):
    t = '-'.join(title.split(' '))
    return t.lower()


# downloading the image
def download_image(url, download_path, pageNum):
    if not os.path.exists(download_path):
        os.makedirs(download_path)
    img_name = add_zeros(str(pageNum)) + FILE_EXT
    img_path = download_path + img_name
    request = send_request(url, True)
    with open(img_path, 'wb') as file_path:
        request.raw.decode_content = True
        shutil.copyfileobj(request.raw, file_path)
    print('Downloading page ' + str(pageNum))


# creating the url of the webpage which contains the manga, chapter and page
def get_page_url(mangaTitle, chapterNum, pageNum=1):
    mangaT = nameChanger(mangaTitle)
    return PROVIDER + mangaT + '/' + str(chapterNum) + '/' + str(pageNum)


# creating the path to which to download the manga scans
def get_path(mangaTitle, chapterNum):
    return LOCAL_PATH + mangaTitle + '/' + chapterNum + '/'


# downloading the actual scans
def download_chapter(mangaTitle, chapterNum):
    current_page = INITIAL_PAGE
    download_path = get_path(mangaTitle, chapterNum)

    if released_or_not(mangaTitle, chapterNum):  # handling exceptions
        print('Not released yet')
        return None
    while True:
        page_url = get_page_url(mangaTitle, chapterNum, current_page)
        request = send_request(page_url)
        raw_html = request.text

        if request.status_code != 200 or not len(raw_html):  # handling except
            print("No such thing" if not len(raw_html) else 'Success')
            break

        parsed_html = bs(raw_html, 'html.parser')  # parsing for images
        img_url = parsed_html.find('img', {'id': 'img'}).get('src')

        download_image(img_url, download_path, current_page)

        current_page = current_page + 1
