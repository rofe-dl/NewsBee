import urllib.parse
import requests
import os

mediastack_url = 'http://api.mediastack.com/v1/news?'
limit = 25
access_key = os.environ['MEDIASTACK_API_KEY']
country_code = "" #to be set before using the functions

def get_result(entered_params):
    params = {
        'access_key': access_key,
        'countries' : country_code,
        'languages' : 'en',
        'sort': 'published_desc',
        'limit' : limit
    }

    #adds the entered_params to params
    for k,v in entered_params.items():
        params[k] = v

    params = urllib.parse.urlencode(params)
    
    res = requests.get(f"{mediastack_url}{params}")
    json = res.json()

    filtered_json = []

    #mediastack sends duplicate news after they've been edited, so filter them by skipping same url
    urls_found = set() 
    for article in json['data']:
        if article['url'] not in urls_found:
            filtered_json.append(article)
            urls_found.add(article['url'])

    return filtered_json

def get_by_country():
    return get_result({}) #passes empty dictionary as arg

def get_by_keyword(keyword):
    entered_params = {
        'keywords' : keyword
    }

    return get_result(entered_params)