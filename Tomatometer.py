from requests_html import HTMLSession
from bs4 import BeautifulSoup
import json
# The package only supports Python Version 3.6 and above at the moment, so it might not work with another version.

# def get_tomatometer_rating(url):

url='https://www.rottentomatoes.com/m/black_adam'
s = HTMLSession()
response = s.get(url)
# print('Hi')
response.html.render(timeout=20)
# print('Hi')
soup = BeautifulSoup(response.content,'html.parser')
# print('Hi')
# movie_divs = soup.select('div.lister-item.mode-advanced')
# names = [tag.find('h3',class_='lister-item-header').find('a').text for tag in movie_divs]
# print(names[0])

data = json.loads(soup.find('script', type='application/ld+json').string)
# print(data)
print(data['aggregateRating']['ratingValue'])  
