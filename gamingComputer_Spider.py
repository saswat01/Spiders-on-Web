import requests
from bs4 import BeautifulSoup

url = "https://www.newegg.com/global/in-en/p/pl?d=gaming+laptop&cm_sp=KeywordRelated-_-gaming%20laptops-_-gaming%20laptop-_-INFOCARD"
page = requests.get(url, timeout = 5)
soup = BeautifulSoup(page.content, "html.parser")

out_file = "gaming_computers.csv"
header = "Gaming_Computers"

#f = open(out_file, "w")
#f.write(header)
name = soup.findAll("a", {"class":"item-title"})
count = 0
for computers in name:
	count+=1
	if count>4:
		print(computers.text)
		#f.write(computers.text)
	else:
		pass
#print(name)