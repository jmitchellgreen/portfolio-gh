from Post import Post
from bs4 import BeautifulSoup
import os
from datetime import date


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

            # clean date from Title
            title = soup.h1.text
            if ", 20" in title:
                title = title[:-6]

            archive_obj = {
                "url": file[:-5],
                "title": title,
                "thumbnail": "static/" + soup.img["src"][31:-5],
                "tags": tags,
                "date": date.fromisoformat(soup.h2.text),
            }

            my_archive.append(archive_obj)

    sorted_obj = sorted(my_archive, key=lambda archive: archive["date"], reverse=True)
    return sorted_obj
