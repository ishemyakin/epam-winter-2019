import json
import requests
import re
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top"
resp = requests.get(url)
soup = BeautifulSoup(resp.text, "lxml")



fullres={}
for elem in soup.find_all(class_="titleColumn"):
    regdict = re.findall(r'\d+', elem.get_text())
    act_list = tuple(map(str, elem.a['title'].split('(dir.), ')))
    movie_position = regdict[0]
    movie_name = elem.a.string
    movie_year = elem.span.string
    rating = elem.parent.strong.text

    res = {
        "Position": movie_position,
        "Year": movie_year,
        "Director": act_list[0],
        "Crew":  act_list[1],
        "Rating": rating
        }
    fullres.update({movie_name: res})


with open ("test.json", "w") as json_file:
    result = json.dump(fullres, json_file)

print(fullres['Начало'])
