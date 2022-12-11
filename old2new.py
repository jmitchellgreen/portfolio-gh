from Post import Post
from bs4 import BeautifulSoup

# print(inspect.getfullargspec(Post().__init__).annotations)
with open("old_site.html") as fp:
    soup = BeautifulSoup(fp, features="html.parser")

projects = soup.find_all("div", class_="project")


each_proj = [i for i in projects]

for proj in each_proj:
    url = proj.span.text
    title = proj.h3.text
    tags = proj.h4.text
    content = proj.p.text
    try:
        img = proj.img["src"]
        file_path = img.split("/")
        image = file_path[-1]
    except:
        continue
    p = Post(url=url, title=title, tags=tags, thumbnail=image, content=content)
    p.create_post()
