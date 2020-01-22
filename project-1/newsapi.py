import requests
import pprint
url = ('https://newsapi.org/v2/everything?'
       'q=US+President+Election&'
       #'country=us&'
       'apiKey=b345278d3d5b441f86a77122d28ffc74')
response = requests.get(url)
response = response.json()
#pprint.pprint(response)
myurl = []
for j in range(len(response['articles'])):
    myurl.append(response['articles'][j]['url'])

print(myurl)
