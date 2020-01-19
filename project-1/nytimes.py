from nytimesarticle import articleAPI
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

def get_articles(date_year,query):
    all_articles = []
    for i in range(0,10):
        articles = api.search(q = query,
               begin_date = int(date_year + '0101'),
               end_date = int(date_year + '1231'),
               page = i)
        time.sleep(6)
        for j in range(len(articles['response']['docs'])):
            article = articles['response']['docs'][j]['web_url']
            print(article)
            all_articles.append(article)
    print(all_articles)
    return all_articles


all = []
for i in range(2017,2018):
    year = get_articles(str(i),'Obama')
    all = all + year


# keys = all[0].keys()
# with open('nytimes.csv', 'wb') as output_file:
#     dict_writer = csv.DictWriter(output_file, keys)
#     dict_writer.writeheader()
#     dict_writer.writerows(all)
