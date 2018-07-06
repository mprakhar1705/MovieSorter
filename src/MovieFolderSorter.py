import requests
from bs4 import BeautifulSoup
import os

path = "F:\PythonProjects\MovieSorter\src\movie"

os.chdir(path)
movie_list = os.listdir()

base_url = "https://www.imdb.com/search/title?title="
for movie in movie_list:
    movie_name = os.path.splitext(movie)[0]

    movie_name = movie_name.split(" ")
    movie_name = "+".join(movie_name)


    url = base_url + movie_name

    r = requests.get(url)

    soup = BeautifulSoup(r.content, "html.parser")

    data = soup.find("div", {"class": "lister-item mode-advanced"})
    rating = data.find("div", {"class": "inline-block ratings-imdb-rating"})
    os.rename(movie, str(float(rating['data-value']))+"-"+movie)
