from NYTimesArticleAPI import articleAPI  # need to use local, manually copied package for now
import pprint
import json
import time
import csv

api = articleAPI('qbQh29tAn22AwG80h8MfRUNxucW1kcTi')

# articles = api.search(q="Obama",page=99, begin_date=20111231)
# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(articles['response']['docs'])


# def parse_articles(articles):
#     '''
#     This function takes in a response to the NYT api and parses
#     the articles into a list of dictionaries
#     '''
#     news = []
#     print(articles)
#     for i in articles['response']['docs']:
#         dic = {}
#         dic['id'] = i['_id']
#         if i['abstract'] is not None:
#             dic['abstract'] = i['abstract'].encode("utf8")
#         dic['headline'] = i['headline']['main'].encode("utf8")
#         dic['desk'] = i['news_desk']
#         dic['date'] = i['pub_date'][0:10] # cutting time of day.
#         dic['section'] = i['section_name']
#         if i['snippet'] is not None:
#             dic['snippet'] = i['snippet'].encode("utf8")
#         dic['source'] = i['source']
#         dic['type'] = i['type_of_material']
#         dic['url'] = i['web_url']
#         dic['word_count'] = i['word_count']
#         # locations
#         locations = []
#         for x in range(0,len(i['keywords'])):
#             if 'glocations' in i['keywords'][x]['name']:
#                 locations.append(i['keywords'][x]['value'])
#         dic['locations'] = locations
#         # subject
#         subjects = []
#         for x in range(0,len(i['keywords'])):
#             if 'subject' in i['keywords'][x]['name']:
#                 subjects.append(i['keywords'][x]['value'])
#         dic['subjects'] = subjects
#         news.append(dic)
#     print(news)
#     return(news)

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
            fq = {'body': ["US", "presidential", "election"],
                  'subject': ['Presidential Election of {}'.format(election_yr),
                              'Presidential Election of {}'.format(next_election_yr),
                              'Presidents and Presidency (US)']},
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


all_articles = []

# NOTE: doesn't like ES OR or AND, due to bug in library handling of url request format
keyphrase = "election~"
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
        if search_yr < 1851:  # NYT data doesn't go before 1851
            continue
        articles_for_year = get_articles(str(search_yr), keyphrase, election_yr=yr, next_election_yr=next_yr)

        # print intermediate results to console
        if len(articles_for_year) == 0:
            print("No articles for year {}".format(search_yr))
        else:
            print("Articles for year {}:".format(search_yr))
            print(articles_for_year)
            
        all_articles = all_articles + articles_for_year

# print final results to file
with open('output.txt', 'w+') as out:
    out.write(all_articles)


# keys = all[0].keys()
# with open('nytimes.csv', 'wb') as output_file:
#     dict_writer = csv.DictWriter(output_file, keys)
#     dict_writer.writeheader()
#     dict_writer.writerows(all)
