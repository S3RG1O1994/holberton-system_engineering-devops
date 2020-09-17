#!/usr/bin/python3
'''Function for obtain users an subscribers'''
import requests


def top_ten(subreddit):
    '''Query in the API reddit an return the number of subscribers'''
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-agent': 'Chrome/85.0.4183.102'}
    query = requests.get(url, headers=headers, allow_redirects=False)
    file = query.json().get('data')
    if query.status_code == 200:
        for i in file['children']:
            print(i['data']['title'])
    print (None)
