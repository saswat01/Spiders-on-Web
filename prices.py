#This code finds out all the prices of GPUs from newegg website
import requests
from bs4 import BeautifulSoup 

url = "https://www.newegg.com/global/in-en/p/pl?d=graphics+card"

#Grabs the content from the URL
page = requests.get(url, timeout = 5)

#Parsing the HTML
soup = BeautifulSoup(page.content, "html.parser")

#Searches for all the div tags with class item-action
container = soup.findAll("div",{"class":"item-action"})

#Finds all the prices of the GPUS
for contains in container:
    x = contains.findAll("li", {"class":"price-current"})
    product_cost = x[0].text
    print(product_cost)

