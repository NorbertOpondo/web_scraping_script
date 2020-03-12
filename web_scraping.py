from selenium import webdriver
import pandas as pd
from requests_html import HTMLSession
from bs4 import BeautifulSoup

session = HTMLSession()
#driver = webdriver.Firefox()

products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
response = session.get('https://www.jumia.co.ke/mens-watches/')

#content = driver.page_source
soup = BeautifulSoup(response.content,"html.parser")
for a in soup.findAll('div', attrs={'class':'sku -gallery'}):
	name=a.find('span', attrs={'class':'name'}).text
	price=a.find('span', attrs={'class':'price'}).text
	products.append(name)
	prices.append(price)

df = pd.DataFrame({'Product Name':products,'Price':prices}) 
df.to_csv('products.csv', index=False, encoding='utf-8')