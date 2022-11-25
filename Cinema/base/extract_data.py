import requests
from bs4 import BeautifulSoup
import json
from requests_html import HTMLSession
from base.save import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

# Creating our database

### Extracts all movie information from the IMDB urls
def extract_all():
    url1 = 'https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating,desc&start=1&ref_=adv_nxt&count=250'
    url2 = 'https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating,desc&start=251&ref_=adv_nxt&count=250'
    extract(url1)
    extract(url2)

# Given a url, it extracts information of all movies in it
def extract(url):

    # Making a GET request, and parse the html content with Beautiful Soup
    response = requests.get(url)
    soup = BeautifulSoup(response.content,'html.parser')

    # List of 'div's containing the information of all movies
    movie_divs = soup.select('div.lister-item.mode-advanced')

    # List of movie titles
    names = [tag.find('h3',class_='lister-item-header').find('a').text for tag in movie_divs]
    
    # List of movie release years
    years = [tag.find('h3',class_='lister-item-header').find('span',class_='lister-item-year text-muted unbold').text.replace('(','').replace(')','') for tag in movie_divs]

    # List of movie links to its particular imdb page
    links = ['https://www.imdb.com/'+tag.find('h3',class_='lister-item-header').find('a')['href'] for tag in movie_divs]
    
    # List of title image of movies
    imgs = [json.loads(BeautifulSoup(requests.get(url).content,'html.parser').find('script', type='application/ld+json').string)['image'] for url in links]

    runtimes = [tag.find('p',class_='text-muted').find('span',class_='runtime').text.replace('\n','') for tag in movie_divs]

    # List of list of movie genres
    genres = [tag.find('p',class_='text-muted').find('span',class_='genre').text.replace('\n','').replace('  ','') for tag in movie_divs]

    # List of movie's IMDB rating
    imdb_ratings = [tag.find('strong').text.replace('  ','') for tag in movie_divs] 

    # Returns movie's Metascore  = Metacritic rating 
    def meta_rating_finder(movie):
        try:
            # Not all movies have the following element, hence may produce error
            # Dealt using try except
            rating =  movie.find('span',class_='metascore').text.replace('  ','')
            return rating
        except:
            return None

    # List of movie's Metascore
    meta_ratings = [meta_rating_finder(movie) for movie in movie_divs]

    # List of movie's plot
    plots = [movie.select('p.text-muted')[1].text.replace('\n','') for movie in movie_divs]

    # List of list of movie's directors
    directors = [movie.select('p')[2].text.replace('\n','').replace('  ','').split('| ')[0].split(':')[1] for movie in movie_divs]

    # List of list of movie's starring actors
    stars = [movie.select('p')[2].text.replace('\n','').replace('  ','').split('| ')[1].split(':')[1] for movie in movie_divs]

    # Saving all the data to database
    for i in range(len(movie_divs)):
        movies_info = {'name':names[i], 'year':years[i],'runtime':runtimes[i], 'genre':genres[i], 'imdb':imdb_ratings[i], 'meta':meta_ratings[i],
                    'plot':plots[i], 'directors':directors[i], 'stars': stars[i],'img':imgs[i],'extra_details':getDetails(names[i],plots[i]), 'trailer':getTrailer(names[i]),
                    'reviews':get_reviews(names[i]),'user_reviewsIMDB':getUserReviews_imdb(links[i]),'user_reviewsMeta':getUserReviews_meta(names[i]) } 
                    
        # Defined in save.py
        save(movies_info)

### Extracting details from Rotten Tomatoes
# Returns details of a movie, given name and plot
def getDetails(name,plot):
    # Generates the url to the movie's rotten tomato page
    url = 'https://www.rottentomatoes.com/m/' + name.lower().replace(": ","_").replace(' ','_').replace('-',"_").replace('\'','').replace('!','')
    
    response = requests.get(url)
    print('Scraping:', name)

    # Upon successful connection
    if response.status_code==200:
        soup = BeautifulSoup(response.content,'html.parser')
        dictionary = {} # We return this dictionary containing all the movie details
        
        # Scrapes TomatoMeter of the movie
        try:
            data = json.loads(soup.find('script', type='application/ld+json').string)
            dictionary['tomatometer']=(data['aggregateRating']['ratingValue']) 
        except:
            dictionary['tomatometer']=None

        # Scrapes of gallery images for the movie
        gal=soup.select('img.PhotosCarousel__image')
        gallery=[tag['src'] for tag in gal]
        dictionary['gallery']=gallery

        # Scrapes summary of the movie
        summary = soup.find('div',id='movieSynopsis').text.replace('  ','').replace('\n','')
        dictionary['summary'] = summary

        # Scraping all other info
        content = soup.select('li.meta-row.clearfix')
        details = {}
        for c in content:
            c = c.text.replace('  ','').replace('\n','').split(':')
            details[c[0]] =  c[1]
            for ch in c[2:]:
                details[c[0]] += ':'+ch
        dictionary['details'] = details

        # Of those other info, extracting language information
        language = ''
        if 'Original Language' in details.keys():
            language = details['Original Language']
        elif 'Language' in details.keys():
            language = details['Language']
        dictionary['lang'] = language
        return dictionary
    else:
        # When no corresponding tomatometer page exists
        return {'img':'https://motivatevalmorgan.com/wp-content/uploads/2016/06/default-movie.jpg',
        'lang':"English",
        'details':{},
        'summary':plot,
        'gallery':[],
        'tomatometer':None,
        }

### Extracting trailer from Metacritic
# Returns link to the trailer video
def getTrailer(name):
    # Generates metacritic page url of the movie
    url='https://www.metacritic.com/movie/'+ name.lower().replace(": ","-").replace(' ','-').replace('_',"-").replace('\'','').replace('!','')
    # Dictionary of HTTP Headers to send with the Request.
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
    
    #Scrapes video link
    try:
        response = requests.get(url,headers=headers)
        soup=BeautifulSoup(response.content, 'lxml')
        video = soup.find('div',id='videoContainer_wrapper')['data-mcvideourl']
        return video
    except:
        #Not available image
        return 'https://thumbs.dreamstime.com/b/not-available-stamp-seal-watermark-distress-style-designed-rectangle-circles-stars-black-vector-rubber-print-title-138796185.jpg'

### Extracting critic Reviews from Rotten Tomatoes
# Returns critic_reviews
def get_reviews(name):
    url="https://www.rottentomatoes.com/m/"+ name.lower().replace(' ','_').replace('-',"_").replace(": ","_").replace('\'','').replace('!','')+"/reviews"
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
    response = requests.get(url,headers=headers)
    if response.status_code==200:
        soup=BeautifulSoup(response.content, 'html5lib')
        s=soup.find_all('div',class_="row review_table_row")

        # Dictionary with author-review tuple
        reviews = {}
        count = 0
        for ek in s:
            if count == 2: break
            author = ek.select('a.unstyled.bold.articleLink')[0].text
            review = ek.select('div.the_review')[0].text.replace('  ','').replace('\n','')
            count += 1
            reviews[author] = review
        return reviews
    else:
         return {}

### Extracting User Reviews from IMDB
def getUserReviews_imdb(url):

    url1 = url + 'reviews?sort=curated&dir=desc&ratingFilter=10'

    try:
        drive=webdriver.Chrome()
        drive.get(url1)
        Reviews={}
        rating=drive.find_elements(By.CLASS_NAME,"rating-other-user-rating")
        name=drive.find_elements(By.CLASS_NAME,"display-name-link")
        reviews=drive.find_elements(By.CLASS_NAME,"text")
        count = 0
        for i in range(0,len(reviews)):
            if count == 2:
                break
            try:
                if reviews[i].text=="":
                    WebDriverWait(drive, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.expander-icon-wrapper"))).click()
                    reviews=drive.find_elements(By.CLASS_NAME,"text")
            
                Review={}
                Review['rating']=rating[i].text[:-3]
                Review['name']=name[i].text
                review = reviews[i].text
                Review['less_review']=review[:300]
                Review['more_review']=review[300:]
                Reviews[name[i].text]=Review
                count = count + 1
            except:
                pass


        drive.quit()
        url1=url+"reviews?sort=curated&dir=desc&ratingFilter=1"

        driver=webdriver.Chrome()
        driver.get(url1)
        rating1=driver.find_elements(By.CLASS_NAME,"rating-other-user-rating")
        name1=driver.find_elements(By.CLASS_NAME,"display-name-link")
        reviews1=driver.find_elements(By.CLASS_NAME,"text")
        count=0
        for i in range(0,2):
            if count == 2:
                break
            try:
                if reviews1[i].text=="":
                    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.expander-icon-wrapper"))).click()
                    reviews1=driver.find_elements(By.CLASS_NAME,"text")
                Review={}
                Review['rating']=rating1[i].text[:-3]
                Review['name']=name1[i].text
                review = reviews1[i].text
                Review['less_review']=review[:300]
                Review['more_review']=review[300:]
                Reviews[name1[i].text]=Review
            except:
                pass
        driver.quit()
        return Reviews

    except:
        return {}


def getUserReviews_meta(name):
    
    url = 'https://www.metacritic.com/movie/' +name.lower().replace(": ","-").replace(' ','-').replace('_',"-").replace('\'','').replace('!','')+ '/user-reviews?dist=positive'
    driver=webdriver.Chrome()
    driver.get(url)
    ALL_Reviews={}
    #WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span.toggle_expand_collapse"))).click()
    Reviews={}
    author=driver.find_elements(By.CLASS_NAME,"author")
    meta_score=driver.find_element(By.XPATH,'//*[@id="main_content"]/div[1]/div[3]/div/div[1]/div[6]/div/div[1]/div[1]')
    review=driver.find_elements(By.CLASS_NAME,"review_body")
    Reviews['author']=author[0].text
    Reviews['meta_score']=meta_score.text
    Reviews['review']=review[1].text
    ALL_Reviews[author[0].text]=Reviews
    driver.quit()
    url = 'https://www.metacritic.com/movie/the-shawshank-redemption/user-reviews?dist=negative'
    driver=webdriver.Chrome()
    driver.get(url)
    Reviews={}
    #WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span.toggle_expand_collapse"))).click()
    author=driver.find_elements(By.CLASS_NAME,"author")
    meta_score=driver.find_element(By.XPATH,'//*[@id="main_content"]/div[1]/div[3]/div/div[1]/div[6]/div/div[1]/div[1]')
    review=driver.find_elements(By.CLASS_NAME,"review_body")
    Reviews['author']=author[0].text
    Reviews['meta_score']=meta_score.text
    Reviews['review']=review[1].text
    ALL_Reviews[author[0].text]=Reviews
    driver.quit()
    return ALL_Reviews
