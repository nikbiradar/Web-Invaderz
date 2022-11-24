from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests

def getUserReviews(url):
    # url="https://www.imdb.com/title/tt0053291/"
    url1 = url + 'reviews?sort=curated&dir=desc&ratingFilter=10'
    # print(url1)
    # print('Hi1')
    drive=webdriver.Chrome()
    drive.get(url1)
    #WebDriverWait(drive, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.expander-icon-wrapper"))).click()
    rating=drive.find_elements(By.CLASS_NAME,"rating-other-user-rating")
    name=drive.find_elements(By.CLASS_NAME,"title")
    reviews=drive.find_elements(By.CLASS_NAME,"text")
    if reviews[0].text=="":
        WebDriverWait(drive, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.expander-icon-wrapper"))).click()
        reviews=drive.find_elements(By.CLASS_NAME,"text")

    Reviews={}
    Review={}
    Review['rating']=rating[0].text
    Review['name']=name[0].text
    Review['review']=reviews[0].text
    Reviews[name[0].text]=Review
    drive.quit()
    url1=url+"reviews?sort=curated&dir=desc&ratingFilter=1"
    # print(url1)
    # print('Hi2')
    driver=webdriver.Chrome()
    driver.get(url1)
    rating1=driver.find_elements(By.CLASS_NAME,"rating-other-user-rating")
    name1=driver.find_elements(By.CLASS_NAME,"title")
    reviews1=driver.find_elements(By.CLASS_NAME,"text")
    if reviews1[0].text=="":
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.expander-icon-wrapper"))).click()
        reviews1=driver.find_elements(By.CLASS_NAME,"text")
    Review={}
    Review['rating']=rating1[0].text
    Review['name']=name1[0].text
    Review['review']=reviews1[0].text
    Reviews[name1[0].text]=Review
    
    driver.quit()
    return Reviews

top250url = 'https://www.imdb.com/search/title/?groups=top_250&sort=user_rating'
response = requests.get(top250url)
soup = BeautifulSoup(response.content,'html.parser')

movie_divs = soup.select('div.lister-item.mode-advanced')
links = ['https://www.imdb.com/'+tag.find('h3',class_='lister-item-header').find('a')['href'] for tag in movie_divs]
# print(links[:5])
user_reviews_imdb = [getUserReviews(link) for link in links[:5]]
# for review in user_reviews_imdb:
#     print(review)

# url = 'https://www.imdb.com//title/tt0108052/'
# print(getUserReviews(url))

