import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/search/title/?groups=top_250&sort=user_rating'
response = requests.get(url)
soup = BeautifulSoup(response.content,'html.parser')


movie_divs = soup.select('div.lister-item.mode-advanced')

names = [tag.find('h3',class_='lister-item-header').find('a').text for tag in movie_divs]
# print(names[0])

years = [tag.find('h3',class_='lister-item-header').find('span',class_='lister-item-year text-muted unbold').text.replace('(','').replace(')','') for tag in movie_divs]
# print(years[0])

runtimes = [tag.find('p',class_='text-muted').find('span',class_='runtime').text.replace('\n','') for tag in movie_divs]
# print(runtimes[0])

genres = [tag.find('p',class_='text-muted').find('span',class_='genre').text.replace('\n','').replace('  ','') for tag in movie_divs]
# print(genres[0])

imdb_ratings = [tag.find('strong').text.replace('  ','') for tag in movie_divs] 
# print(imdb_ratings[0])

def meta_rating_finder(movie):
    try:
        rating =  movie.find('span',class_='metascore').text.replace('  ','')
        return rating
    except:
        return -1

meta_ratings = [meta_rating_finder(movie) for movie in movie_divs]
# print(meta_ratings[0])

plots = [movie.select('p.text-muted')[1].text.replace('\n','') for movie in movie_divs]
# print(plots[0])

directors = [movie.select('p')[2].text.replace('\n','').replace('  ','').split('| ')[0].split(':')[1] for movie in movie_divs]
# print(directors[0])
stars = [movie.select('p')[2].text.replace('\n','').replace('  ','').split('| ')[1].split(':')[1] for movie in movie_divs]
# print(actors[0])


movies_info = [{'name':names[i], 'year':years[i], 'runtime':runtimes[i], 'genre':genres[i], 'imdb':imdb_ratings[i], 'meta':meta_ratings[i],
                'plot':plots[i], 'directors':directors[i], 'stars': stars[i] } for i in range(len(movie_divs))]

# print(movies_info[25])

name = names[15]
url = 'https://www.rottentomatoes.com/m/' + name.lower().replace(' ','_')
response = requests.get(url)
soup = BeautifulSoup(response.content,'html5lib')

# print(response.status_code)

img = soup.find('img',class_='posterImage')['src']
print(img)

# rating = soup.find('div',class_='score-board-wrap').text
# print(rating)

summary = soup.find('div',id='movieSynopsis').text.replace('  ','').replace('\n','')
print(summary)

content = soup.select('li.meta-row.clearfix')
details = {}
for c in content:
    c = c.text.replace('  ','').replace('\n','').split(':')
    details[c[0]] =  c[1]
    for ch in c[2:]:
        details[c[0]] += ':'+ch
for key,value in details.items():
    print(key,':',value)


language = ''
if 'Original Language' in details.keys():
    language = details['Original Language']
elif 'Language' in details.keys():
    language = details['Language']
print(language)