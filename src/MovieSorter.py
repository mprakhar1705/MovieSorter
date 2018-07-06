import requests
from bs4 import BeautifulSoup

movie_list = []
base_url = "https://www.imdb.com/search/title?title="

file = open("movies.txt", "r")
file1 = open("sorted_movies.txt", "w")
for line in file:
    movie_name = line.split(" ")
    movie_name = "+".join(movie_name)

    url = base_url + movie_name

    r = requests.get(url)

    soup = BeautifulSoup(r.content, "html.parser")

    all_links = soup.find_all("a")[0]

    data = soup.find("div", {"class": "lister-item mode-advanced"})
    rating = data.find("div", {"class": "inline-block ratings-imdb-rating"})
    movie_list.append([movie_name, rating['data-value']])

sorted_list = sorted(movie_list, key=lambda x: x[1])
sorted_list.reverse()

for i in sorted_list:
    file1.write(i[0].replace("+", " "))
print("Done")
