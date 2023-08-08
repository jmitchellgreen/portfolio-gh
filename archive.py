from bs4 import BeautifulSoup
import os
from datetime import date
import pprint

# depreciated func
def archive2():
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
                "iso_date": date.fromisoformat(soup.h2.text),
                "date": date.fromisoformat(soup.h2.text).strftime("%d %b %y"),
            }

            my_archive.append(archive_obj)

    sorted_obj = sorted(
        my_archive, key=lambda archive: archive["iso_date"], reverse=True
    )
    return sorted_obj


def archive():
    PATH = "./pages/archive/posts"

    files = os.listdir(PATH)

    my_archive = []
    for file in files:
        try:
            with open(f"./pages/archive/posts/{file}") as f:

                # soup for each .html
                soup = BeautifulSoup(f, features="html.parser")

                url = file[:-5]

                title = soup.h1.text
                # remove year in title
                if ", 20" in title:
                    title = title[:-6]

                # format tags new and old
                tags = [
                    tag.text.strip("\n").strip("[").strip("]").split(",")
                    for tag in soup.find_all(class_="tags")
                ]
                tags = tags[0]
                if "\n" in tags[0]:
                    tags[0] = tags[0].replace("\r", "").replace("\n", ",").split(",")
                    tags = tags[0]
                    tags = [t.lstrip() for t in tags]

                tags = [t.strip() for t in tags]

                iso_date = date.fromisoformat(soup.find(class_="date").text)
                if iso_date is None:
                    continue

                archive_obj = {
                    "url": url,
                    "title": title,
                    "tags": tags,
                    "iso_date": iso_date,
                    "date": iso_date.strftime("%Y %b %d"),
                }

                my_archive.append(archive_obj)
        except:
            continue

    sorted_obj = sorted(
        my_archive, key=lambda archive: archive["iso_date"], reverse=True
    )

    removals = [
        "weather4you",
        "wv-map",
        "va-pop-map",
        "qgis-plugin",
        "otter-tail-map",
        "nw-usa-map",
        "install-geopandas",  # for now...
        "ffosm",
    ]

    # remove pages (for now...)
    sorted_obj = [x for x in sorted_obj if x["url"] not in removals]

    return sorted_obj


def change_html():
    PATH = "./pages/archive/posts"

    files = os.listdir(PATH)

    my_archive = []
    for file in files:
        if file == "install-geopandas.html":
            continue
        with open(f"./pages/archive/posts/{file}", "r") as f:

            soup = BeautifulSoup(f, features="html.parser")

            if soup.h2:
                soup.h2["class"] = "date"
            if soup.h1:
                soup.h1["class"] = "title"

        with open(f"./pages/archive/posts/{file}", "w") as f:
            f.write(str(soup))


if __name__ == "__main__":
    change_html()
