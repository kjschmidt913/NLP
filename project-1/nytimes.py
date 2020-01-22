from nytimesarticle import articleAPI
from scrape import scrapeFromURL
import pprint
import json
import time
import csv

api = articleAPI('qbQh29tAn22AwG80h8MfRUNxucW1kcTi')


# Iterate through dates within a year and pages (limit set to 10) to collect article links
def get_articles(date_year, query):
    all_articles = []
    for i in range(0, 10):
        articles = api.search(q=query,
                              begin_date=int(date_year + '0101'),
                              end_date=int(date_year + '1231'),
                              page=i)
        time.sleep(6)
        if (articles['response']):
            for j in range(len(articles['response']['docs'])):
                article = articles['response']['docs'][j]['web_url']
                print(article)
                all_articles.append(article)
    return all_articles


web_urls = []
# Iterate through different years to collect web_urls
for i in range(2010, 2011):
    year = get_articles(str(i), 'Obama')
    web_urls = web_urls + year
print(web_urls)


corpora = scrapeFromURL(web_urls)
print(corpora)

# with open('raw_text.csv', 'w') as result_file:
#     wr = csv.writer(result_file)
#     for item in corpora:
#         wr.writerow([item, ])


result_file = open('raw_text.txt', 'w')

for item in corpora:
    result_file.writelines(item)
