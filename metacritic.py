from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests


url = 'https://www.metacritic.com/movie/the-shawshank-redemption/user-reviews?dist=positive'
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
print(ALL_Reviews)
