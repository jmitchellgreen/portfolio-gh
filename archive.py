from black import mypyc_attr
from Post import Post
from bs4 import BeautifulSoup
import os


def archive():
    PATH = "./pages/archive/posts"

    files = os.listdir(PATH)

    my_archive = []
    for file in files:
        with open(f"./pages/archive/posts/{file}") as f:
            soup = BeautifulSoup(f, features="html.parser")
            archive_obj = {
                "url": file[:-5],
                "title": soup.h1.text,
                "thumbnail": "static/" + soup.img["src"][31:-5],
                "tags": soup.h4.text,
            }
            my_archive.append(archive_obj)

    return my_archive
