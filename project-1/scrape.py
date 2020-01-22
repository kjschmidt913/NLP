from bs4 import BeautifulSoup
import requests

def scrapeFromURL(web_urls):
    corpora = []
    for i in web_urls:
        r = requests.get(i)
        soup = BeautifulSoup(r.content,"html.parser")
        title = soup.find('title')
        title.get_text()
        paragraphs = soup.find_all('p')

        ad0 = "Advertisement"
        ad1 = "Supported by"

        for element in paragraphs:
            if element.text != ad0 and element.text != ad1:
                corpora.append(element.text)
    return corpora
