import requests
from bs4 import BeautifulSoup

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
empires_top_movies = response.text

soup = BeautifulSoup(empires_top_movies, "html.parser")
movies_file_path = "Movies.txt"

top_titles = soup.find_all( class_="article-title-description")

movies_list = []
for title in top_titles:
    movie_title = title.find(class_="title")
    movies_list.append(movie_title.string)

    print(movie_title.get_text(strip=True))
    
# print(list)
movies_list.reverse()

# Open the file in write mode and write each title to a new line
with open(movies_file_path, "w") as file:
    for movie_title in movies_list:
        file.write(f"{movie_title}\n")

print(f"Movie titles have been saved to {movies_file_path}")