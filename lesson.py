from bs4 import BeautifulSoup

import requests

response = requests.get("https://news.ycombinator.com/")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

articles = soup.find_all(name="a", class_="titlelink")
article_text = []
article_links = []
for article_tag in articles:
    text = article_tag.get_text()
    article_text.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [int(score.get_text().split()[0]) for score in soup.find_all(name="span", class_="score")]

index = article_upvotes.index(max(article_upvotes))
print(article_text[index])
print(article_links[index])
print(article_upvotes[index])

# print(article_text)
# print(article_links)
# print(article_upvotes)


# import lxml
#
# with open("website.html", encoding="utf8") as file:
#     contents = file.read()
#
#
# soup = BeautifulSoup(contents, "html.parser")
# all_anchor_tags = soup.find_all(name="a")
#
# for tag in all_anchor_tags:
#     print(tag.get("href"))
#
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.string)
#
# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# name = soup.select_one(selector="#name")
# print(name)
#
# headings = soup.select(selector=".heading")
# print(headings)