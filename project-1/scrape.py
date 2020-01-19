from bs4 import BeautifulSoup
import requests

url = "https://www.nytimes.com/2017/04/16/us/politics/north-korea-missile-crisis-slow-motion.html"

r = requests.get(url)
soup = BeautifulSoup( r.content ,"html.parser")
title = soup.find('title')
title.get_text()
paragraphs = soup.find_all('p')

#print(paragraphs)

ad0 = "Advertisement"
ad1 = "Supported by"
for element in paragraphs:
    if element.text != ad0 and element.text != ad1:
        print(element.text)
