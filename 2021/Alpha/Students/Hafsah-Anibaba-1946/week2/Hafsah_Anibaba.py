# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 06:55:24 2021

@author: Hafsah F. Anibaba
"""

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
pages = []
for url in range (1,51):
    urls = 'http://books.toscrape.com/catalogue/page-'+str(url)+'.html'
    pages.append(urls)
title = []
image = []
price = []
rating = []
for page in pages:
    url = requests.get(page)
    soup = bs(url.content)
    book_section =soup.find('ol', attrs = {'class' : 'row'})
    title_a = book_section.select('h3 a')
    title_ = []
    for i in title_a:
        title_.append(i['title'])
    for i in title_:
        title.append(i)
    Rating_ = book_section.find_all('p', attrs = {'class':'star-rating'})
    s = [s['class'] for s in Rating_]
    rating_ = [a[1] for a in s]
    for i in rating_:
        rating.append(i)
    lst = book_section.select('a img')
    image_ = [s['src'] for s in lst]
    for i in image_:
        image.append(i)
    lst = book_section.find_all('p', attrs ={'class':'price_color'})
    price_ = [s.get_text() for s in lst]
    for i in  price_:
         price.append(i)
df = pd.DataFrame(columns =['Name','Image URL','Price','Rating'])
df['Name'] = title
df['Image URL'] = image
df['Price'] = price
df['Rating'] = rating
print(df)