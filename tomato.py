import requests
from bs4 import BeautifulSoup
r=requests.get("https://www.rottentomatoes.com/m/the_shawshank_redemption/reviews")
soup=BeautifulSoup(r.content,'html5lib')
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
print(reviews)
# print(abc)
# for a in s:
#     items=' '.join(a.text.split())
    # print(items)