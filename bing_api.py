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

    headers = {'Ocp-Apim-Subscription-Key': api_key}
    param = {'q': query, 'count': count}

    response = requests.get(endpoint, headers=headers, params=param)
    response = response.json()

    links_dict = {}
    key = 0

    for i in response["webPages"]["value"]:
        links_dict[str(key)] = str(i['url'])
        key = key + 1

    json_data = json.dumps(links_dict)

    return json_data



