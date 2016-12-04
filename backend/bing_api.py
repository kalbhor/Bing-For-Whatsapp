'''
Searches queries fetched from js through Bing's API
returns json
'''

import json
import requests


def std_search(query, count='3'):
    ''' Standard Bing Search, returns json '''

    api_key = "dc271ed6bd4c4f44bb79399639d7d883"
    endpoint = "https://api.cognitive.microsoft.com/bing/v5.0/search"
    links_dict = {}

    headers = {'Ocp-Apim-Subscription-Key': api_key}
    param = {'q': query, 'count': count}

    try:
        response = requests.get(endpoint, headers=headers, params=param)
        response = response.json()

        key = 0

        for i in response["webPages"]["value"]:
            links_dict[str(key)] = str(i['displayUrl'])
            key = key + 1

        json_data = json.dumps(links_dict)

    except Exception as ex:
        template = "{0} occured."
        message = template.format(type(ex).__name__)

        json_data = json.dumps({'error': message})

    return json_data


def img_search(query, count='3'):
    ''' Bing image search, returns json '''

    api_key = "dc271ed6bd4c4f44bb79399639d7d883"
    endpoint = "https://api.cognitive.microsoft.com/bing/v5.0/images/search"
    links_dict = {}

    headers = {'Ocp-Apim-Subscription-Key': api_key}
    param = {'q': query, 'count': count}

    try:
        response = requests.get(endpoint, headers=headers, params=param)
        response = response.json()

        key = 0

        for i in response['value']:
            links_dict[str(key)] = str((i['contentUrl']))
            key = key + 1

        json_data = json.dumps(links_dict)

    except Exception as ex:
        template = "{0} occured."
        message = template.format(type(ex).__name__)

        json_data = json.dumps({'error': message})

    return json_data
