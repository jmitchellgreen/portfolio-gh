#### Mitchell Green
#### github: jmitchellgreen


from typing import List
import datetime


class Post:
    def __init__(
        self,
        url: str = None,
        title: str = None,
        tags: List[str] = None,
        repo_link: str = None,
        short_desc: str = None,
        thumbnail: str = None,
        content: str = None,
        year: int = datetime.date.today().year,
        custom_page: bool = False,
    ) -> None:
        self.url = url
        self.title = title
        self.tags = tags
        self.repo_link = repo_link
        self.short_desc = short_desc
        self.thumbnail = thumbnail
        self.content = content
        self.year = year
        self.custom_page = custom_page

    def create_post(self) -> None:
        with open(f"./pages/archive/posts/{self.url}.html", "w") as post:
            post.write(
                f"""{{% extends "base.html" %}}
                    {{% block content %}}
                    <main>
                        <!-- Title -->
                        <h1>{self.title}</h1>
                        <!-- Year -->
                        <h2></h2>
                        <!-- Tags -->
                        <div class="tags">
                            <a href="/tags/">
                                <h4 style="display: inline;">{self.tags}</h4>
                            </a>
                        </div>
                        <!-- Thumbnail -->
                        <img src="{{{{ url_for('static', filename='images/{self.thumbnail}') }}}}" alt="">
                        <!-- Content -->
                        <p>{self.content}</p>
                    </main>
                    {{% endblock %}}"""
            )
        return
