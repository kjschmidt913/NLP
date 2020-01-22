from NYTimesArticleAPI import articleAPI  # need to use local, manually copied package for now
from scrape import scrapeFromURL
import pprint
import json
import time
import csv


api = articleAPI('qbQh29tAn22AwG80h8MfRUNxucW1kcTi')

def get_articles(date_year, query, election_yr=2016, next_election_yr=2020):
    """
    Return article URLs about the given elections for the given date year.

    The multiple 'subject' values appear to be OR'd together -- you don't need all of them to match.

    :param date_year: The year to search for news in, from Jan 1 to Dec 31
    :param query: The singular primary query term
    :param election_yr: The election year's news to search for
    :param next_election_yr: The following election year
    :return all_articles: All articles across 10 pages (max 100) for the given search year
    """
    all_articles = []
    page_range = range(0, 10)  # max 99
    for i in page_range:
        # returns 10 results per page
        articles = api.search(
            q = query,
            # fq = {'news_desk':['Politics']
            #       },
            # facet_fields ='news_desk',
            # facet= 'true',
            begin_date = int(date_year + '0101'),
            end_date = int(date_year + '1231'),
            page = i
            )
        # need to sleep so we don't get locked out of NYT
        time.sleep(6)

        # this means we probably hit the NYT ping quota -- skip ahead
        if 'response' not in articles.keys():
            if 'fault' in articles.keys():
                print("Error from API: {}".format(articles['fault']['faultstring']))
            continue

        if len(articles['response']['docs']) > 0:
            for j in range(len(articles['response']['docs'])):
                article = articles['response']['docs'][j]['web_url']
                # print(article)
                all_articles.append(article)

    # print(all_articles)
    return all_articles


web_urls = []
# NOTE: doesn't like ES OR or AND, due to bug in library handling of url request format
keyphrase = "US+Russia+Politics"
# start in 1968 cuz we don't get data with our 'fq' params before then
election_years = range(1968, 2016, 4) # step every 4 years

for yr in election_years:
    # the following election year
    next_yr = yr + 4
    # the current year we're searching for news in
    search_yr = yr
    # 0-4 for each year between election years
    for i in range(0, 4):
        search_yr = yr + i
        print(search_yr)
        if search_yr < 1851:  # NYT data doesn't go before 1851
            continue
        urls_for_year = get_articles(str(search_yr), keyphrase, election_yr=yr, next_election_yr=next_yr)

        # print intermediate results to console
        if len(urls_for_year) == 0:
            print("No articles for year {}".format(search_yr))
        else:
            print("Articles for year {}:".format(search_yr))
            print(urls_for_year)
            
        web_urls = web_urls + urls_for_year

# print final results to file
with open('urls_output.txt', 'w+') as out:
    for item in web_urls:
        out.write(item + '\n')

# get all raw text coropora from NYT links
corpora = scrapeFromURL(web_urls)
print(corpora)
result_file = open('raw_text.txt', 'w')

for item in corpora:
    result_file.writelines(item)

