import requests

from bs4 import BeautifulSoup

URL = "https://online-samsung.ru/catalog/smartfony/"

page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

post = soup.find("div" )
#post_id = post["id"]
print(post)
print(soup.div.title)

#title = post.find("a", class_="post__title_link").text.strip()
#description = post.find("div", class_="post__text post__text-html post__text_v1").text.strip()
#url = post.find("a", class_="post__title_link", href=True)["href"].strip()

#print(title, description, url)