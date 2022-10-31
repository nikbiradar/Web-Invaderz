# from multiprocessing import connection
# from urllib import response
import requests
from bs4 import BeautifulSoup
import sys, sqlite3

#===========================
#Do i need a session?
#Should i login anywhere?
#Are sessions only when login/logour is invloved?
#What are sessions?
#========================
url = sys.argv[1]
response = requests.get(url)
soup = BeautifulSoup(response.content,'html.parser')
print(f"Successfully Acquired content from \"{soup.title.text}\"")

#titletags
titletags = soup.select('td.titleColumn')
movies = [tag.find('a').text for tag in titletags]
years = [tag.find('span').text.replace('(','').replace(')','') for tag in titletags]
actors = [tag.find('a')['title'] for tag in titletags]

#ratingtags
ratingtags = soup.select('td.ratingColumn.imdbRating')
ratings = [tag.text.replace('\n','') for tag in ratingtags]

# connection = sqlite3.connect('abc.db')
connection = sqlite3.connect('movieInfoDB.db')

cursor = connection.cursor()

print(f"Successfully extablished connection with the Database")
for i in range(len(movies)):
    cursor.execute(
        '''
        REPLACE INTO IMDBmovieInfo(movie_name, year, actors, rating) VALUES(?,?,?,?)
        ''',(movies[i],years[i],actors[i],ratings[i])
    )

print(f"All insertions performed successfully")
print('==============================================')
# movies = cursor.execute(
#     '''
#     SELECT *
#     FROM IMDBmovieInfo
#     '''
# ).fetchall()

# for movie in movies:
#     print(movie)
# We shall store information as classes?
# A movie class?

connection.commit() 
#Essential to save it into database instead of just doing stuff temporarily
connection.close()
