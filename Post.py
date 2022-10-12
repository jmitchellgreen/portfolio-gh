#### Mitchell Green
#### github: jmitchellgreen


from typing import List
import datetime
import inspect
import os
import sys
import json


class Post:
    def __init__(
        self,
        url: str = None,
        title: str = None,
        tags: List[str] = None,
        repo_link: str = None,
        short_desc: str = None,
        thumbnail: str = None,
        year: int = datetime.date.today().year,
        custom_page: bool = False,
    ) -> None:
        self.url = url
        self.title = title
        self.tags = tags
        self.repo_link = repo_link
        self.short_desc = short_desc
        self.thumbnail = thumbnail
        self.year = year
        self.custom_page = custom_page
        self.create_post()

    def create_post(self) -> None:
        if self.url is not None:
            archive_path = "pages\\archive\\"
            mypath = os.path.join(archive_path, self.url)
            if not os.path.isdir(mypath):
                os.makedirs(mypath)


# Post __init__ args
# print(inspect.getfullargspec(Post().__init__).annotations)


if __name__ == "__main__":
    my_url = str(sys.argv[1])
    p = Post(url=my_url)
    with open(
        os.path.join(f"pages\\archive\\{p.url}", "setting.json"), "w"
    ) as settings:
        json.dump(p.__dict__, settings)
