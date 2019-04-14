import tkinter as tk
from manga_scraper import *
import os
from threading import Thread

LOCAL_PATH = '/home/grzegorz/Manga'


class Foundation(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, *kwargs)
        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        frame = StartPage(container, self)
        self.frames[StartPage] = frame
        frame.grid(row=0, column=0, sticky='nsew')
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label1 = tk.Label(self, text='Choose the manga')
        self.label1.pack()
        self.entry1 = tk.Entry(self, bg='white', fg='black', bd=2, w=20)
        self.entry1.pack()
        self.label2 = tk.Label(self, text='Choose the chapter')
        self.label2.pack()
        self.entry2 = tk.Entry(self, bg='white', fg='black', bd=2, w=10)
        self.entry2.pack()
        self.button = tk.Button(self, text='Download', command=self.get_input)
        self.button.pack()

    def get_input(self):
        self.manga_title = self.entry1.get()
        self.manga_chapter = self.entry2.get()
        thread = Thread(target=download_chapter,
                        args=(self.manga_title, self.manga_chapter))
        thread.start()
        thread.join()


app = Foundation()
app.mainloop()
