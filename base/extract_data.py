import requests
from bs4 import BeautifulSoup

def extract():
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
                    'plot':plots[i], 'directors':directors[i], 'stars': stars[i],'extra_details':getDetails(names[i],plots[i]), 'trailer':getTrailer(names[i]),
                    'reviews':get_reviews(names[i]) } for i in range(len(movie_divs))]

    # print(movies_info[25])
    return movies_info


# print(movies_info[25])
def getDetails(name,plot):
# name = names[15]
    url = 'https://www.rottentomatoes.com/m/' + name.lower().replace(' ','_')
    response = requests.get(url)
    soup = BeautifulSoup(response.content,'html.parser')
    print(name)
    if response.status_code==200:

# print(response.status_code)
        dictionary = {}
        img = soup.find('img',class_='posterImage')['src']
        dictionary['img'] = img

        gal=soup.select('img.PhotosCarousel__image')
        gallery=[tag['src'] for tag in gal]
        dictionary['gallery']=gallery

        # rating = soup.find('div',class_='score-board-wrap').text
        # print(rating)

        summary = soup.find('div',id='movieSynopsis').text.replace('  ','').replace('\n','')
        # print(summary)
        dictionary['summary'] = summary

        content = soup.select('li.meta-row.clearfix')
        details = {}
        for c in content:
            c = c.text.replace('  ','').replace('\n','').split(':')
            details[c[0]] =  c[1]
            for ch in c[2:]:
                details[c[0]] += ':'+ch
        dictionary['details'] = details


        language = ''
        if 'Original Language' in details.keys():
            language = details['Original Language']
        elif 'Language' in details.keys():
            language = details['Language']
        dictionary['lang'] = language
        return dictionary

    else:
        return {'img':'https://motivatevalmorgan.com/wp-content/uploads/2016/06/default-movie.jpg',
        'lang':"",
        'details':{},
        'summary':plot,
        'gallery':[],
        }
    
def getTrailer(name):
    url='https://www.metacritic.com/movie/'+ name.lower().replace(' ','-')
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
    try:
        response = requests.get(url,headers=headers)
        soup=BeautifulSoup(response.content, 'lxml')
        video = soup.find('div',id='videoContainer_wrapper')['data-mcvideourl']
        return video
    except:
        return 'https://thumbs.dreamstime.com/b/not-available-stamp-seal-watermark-distress-style-designed-rectangle-circles-stars-black-vector-rubber-print-title-138796185.jpg'



def get_reviews(name):
    url="https://www.rottentomatoes.com/m/"+ name.lower().replace(' ','_')+"/reviews"
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
    response = requests.get(url,headers=headers)
    if response.status_code==200:
        soup=BeautifulSoup(response.content, 'html5lib')
        s=soup.find_all('div',class_="row review_table_row")

        reviews = {}
        count = 0
        for ek in s:
            if count == 2: break
            author = ek.select('a.unstyled.bold.articleLink')[0].text
            # print(author)
            review = ek.select('div.the_review')[0].text.replace('  ','').replace('\n','')
            # print(review)
            count += 1
            reviews[author] = review
        return reviews
    else:
         return {}



