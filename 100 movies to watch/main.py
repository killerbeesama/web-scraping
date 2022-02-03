import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

r = requests.get(url=URL)
movie_data = r.text

soup = BeautifulSoup(movie_data,'html.parser')
find_movies = soup.find_all(name='h3', class_='title')
movie_list = [i.get_text() for i in find_movies][::-1]

with open("movies.txt", mode='w', encoding='utf-8') as file:
    for i in movie_list:
        data_list = file.write(f"{i}\n")

