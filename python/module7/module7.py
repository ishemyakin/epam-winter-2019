import json
import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top"
resp = requests.get(url)

soup = BeautifulSoup(resp.text, "lxml")

a = 0

fullres=[]
for elem in soup.find_all(class_="titleColumn"):
    # print(elem.name)
    # pos
    # name = elem.a.text
    # print(movie_pos)
    movie_name = elem.a.string
    movie_year = elem.span.string
    act_list = tuple(map(str, elem.a['title'].split('(dir.), ')))
    # movie_rating = elem.find(class_="ratingColumn imdbRating").text
    a += 1
    res = {
        "Position": a,
        "Year": movie_year,
        "Director": act_list[0],
        "Crew":  act_list[1],
        "Rating": '10'
        }
    fullres.append({movie_name: res})



    # print(movie_pos, movie_name, movie_rating, movie_year, act_list[0], act_list[1], sep=' --- ',  )
    # print(k[1])
    # print(k[2])


print(fullres[0])

# with open("IMDb Top 250 - IMDb.html", "r") as index_file:
#     soup = BeautifulSoup(index_file, "lxml")
#
# for elem in soup.body.descendants:
#     print(elem.name)

# /html/body/div[2]/div/div[2]/div[3]/div/div[1]/div/span/div/div/div[3]/table/tbody/tr[1]/td[2]

# print(soup.body.table.tbody.parents)
# #
# for elem in soup.body.table.tbody.parents:
#     print(elem.name)
    # print(type(elem))




#
# # imdb_url = "https://www.imdb.com/chart/top/"
# test_url = "https://www.imdb.com/chart/top/"
#
# response = response.get(f"{test_url}/index.html")
#
# print(response)
