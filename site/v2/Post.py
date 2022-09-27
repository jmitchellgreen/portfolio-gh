#### Mitchell Green
#### github: jmitchellgreen


from typing import List
import datetime


class Post:
    def __init__(
        self,
        custom_page: bool = False,
        title: str = None,
        tags: List[str] = [],
        year: int = datetime.date.today().year,
        has_repo: bool = False,
        repo_link: str = None,
        short_desc: str = None,
        thumbnail: str = None,
    ) -> None:
        self.custom_page = custom_page
        self.title = title
        self.tags = tags
        self.year = year
        self.has_repo = has_repo
        self.repo_link = repo_link
        self.short_desc = short_desc
        self.thumbnail = thumbnail
