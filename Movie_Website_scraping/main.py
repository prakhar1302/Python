import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
movies_data = response.text

soup = BeautifulSoup(movies_data,'html.parser')
movies = [movie.getText() for movie in soup.find_all(name='h3',class_='title')]
# print(movies)

# writing in a file
with open(file='movie.text',mode='w') as data:
    for i in range(99,-1,-1):
        data.write(movies[i]+"\n")


