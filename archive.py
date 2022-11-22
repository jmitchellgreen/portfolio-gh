from Post import Post
from bs4 import BeautifulSoup
import os


def archive():
    PATH = "./pages/archive/posts"

    files = os.listdir(PATH)

    my_archive = []
    for file in files:
        with open(f"./pages/archive/posts/{file}") as f:

            # soup for each .html
            soup = BeautifulSoup(f, features="html.parser")

            # parse and cleanup tags to list
            all_tags = soup.h4.text
            all_tags = all_tags.lstrip("[")
            all_tags = all_tags.rstrip("]")
            tags = all_tags.split(",")
            tags = [x.strip() for x in tags]

            archive_obj = {
                "url": file[:-5],
                "title": soup.h1.text,
                "thumbnail": "static/" + soup.img["src"][31:-5],
                "tags": tags,
            }
            my_archive.append(archive_obj)

    return my_archive
