import unittest
from manga_scraper import add_zeros, nameChanger, get_page_url, get_path

class manga_scraper_tests(unittest.TestCase):
	def test_is_nameChanger_working_coorectly1(self):
		self.assertEqual(nameChanger('The Promised Neverland'), 'the-promised-neverland')

	def test_is_nameChanger_working_correctly2(self):
		self.assertEqual(nameChanger('To-LOVE Ru'), 'to-love-ru')

	def test_is_nameChanger_working_correctly3(self):
		self.assertEqual(nameChanger('Tensei Shitara Slime Datta Ken'), 'tensei-shitara-slime-datta-ken')

	def is_add_zeros_working_correctly1(self):
		self.assertEqual(add_zeros('78'), '078')

	def is_add_zeros_working_correctly2(self):
		self.assertEqual(add_zeros('3'), '003')

	def is_add_zeros_working_correctly3(self):
		self.assertEqual(add_zeros('789'), '789')

	def is_get_page_url_working_correctly(self):
		self.assertEqual(get_page_url('Gintama', '22', '7'), 'http://www.mangareader.net/gintama/22/7')

	def is_get_path_working_correctly(self):
		self.assertEqual(get_path('Itoshi no Karin', '5'), '/home/grzegorz/Pulpit/Manga/Itoshi no Karin/5/')


if __name__=='__main__':
	unittest.main()


