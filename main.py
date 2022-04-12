from bs4 import BeautifulSoup

import requests

endpoint = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(endpoint)
movie_webpage = response.text

soup = BeautifulSoup(movie_webpage, "html.parser")

movies = [movie.get_text() for movie in soup.find_all(name="h3", class_="title")[::-1]]

print(movies)

with open("movies.txt", "w", encoding="utf8") as file:
    for movie in movies:
        file.write(f"{movie}\n")