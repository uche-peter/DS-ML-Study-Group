import requests
from bs4 import BeautifulSoup as bs
import re

url = 'http://books.toscrape.com/catalogue/'

'''
#Get the html code and save in txt file by traversing through all the 50 pages
#NB: run only once with data connected
f = open('books-page.txt','ab')
for i in range(1,51):
	src = requests.get(url + 'page-' + str(i) + '.html')
	f.write(src.content)
f.close()
'''
#create an instance of bs from the txt file saved above

bookpage = bs(open('/storage/emulated/0/jupyter/DSC/books-page.txt', 'rb').read(), features = 'html.parser')

#Have a look into the content
#print(bookpage.find('body').prettify())

'''Notice each page has 20 books
stored in an ordered list of class 'row'
Get all pages and store them in a variable'''
books_pages = bookpage.select('ol.row')

#create a variable to store features of each book
data = []

#create column heads
cols = ['Name', 'Image Url', 'Price', 'Rating']

#traverse through pages
for page in books_pages:
	#get all the list items in the page (books)
	books = page.find_all('li')
	#for each book get the required fields
	for book in books:
		temp = book.select('div.image_container a img')[0]
		bk_title = temp['alt']
		bk_url = temp['src']
		bk_price = book.select('div.product_price p')[0].get_text()
		bk_rating = book.find('p', attrs = {'class': re.compile('star-rating')})['class'][1]
		#append the fields list into data
		data.append([bk_title,bk_url,bk_price,bk_rating])

#create pandas using the data variable	
import pandas as pd
df = pd.DataFrame(data, columns = cols )

print(df.head(10))

def to_int(x):
	return {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}[x]

#convert Rating to integers using the fxn above
df['Rating'] = df['Rating'].apply(to_int)

print(df.sample(25))
