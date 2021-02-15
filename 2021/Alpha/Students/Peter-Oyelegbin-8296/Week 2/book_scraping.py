# Book Scraping 50 pages (1000)
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


titles = [] # List to store name of the titles
images = [] # List to store name of the images
prices = [] # List to store price of the product
ratings = [] # List to store rating of the product

for i in range(1, 51):     #Number of pages plus one
    url = "https://books.toscrape.com/catalogue/page-{}.html".format(i)
    r = requests.get(url)

    # Convert to a beautiful soap object
    soup = bs(r.content, "lxml")
    
    for a in soup.find_all('article', attrs = {'class':'product_pod'}):
        name = a.find('h3').find('a')
        image = a.find('img')
        price = a.find('p', attrs = {'class':'price_color'})
        rating = a.find('p', attrs = {'class':'star-rating'})
        titles.append(name["title"])
        images.append(image["src"])
        prices.append(price.text)
        ratings.append(str(rating["class"])[17:-2])
    
books = pd.DataFrame({'Title':titles, 'Image':images, 'Price':prices, 'Rating':ratings})
print(books)
