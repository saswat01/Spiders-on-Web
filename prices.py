#!/usr/bin/env python
# coding: utf-8

# In[31]:


import requests
from bs4 import BeautifulSoup 

url = "https://www.newegg.com/global/in-en/p/pl?d=graphics+card"

page = requests.get(url, timeout = 5)

soup = BeautifulSoup(page.content, "html.parser")

container = soup.findAll("div",{"class":"item-action"})

for contains in container:
    x = contains.findAll("li", {"class":"price-current"})
    product_cost = x[0].text
    print(product_cost)

