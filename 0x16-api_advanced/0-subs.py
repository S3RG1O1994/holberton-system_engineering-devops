#!/usr/bin/python3
'''Function for obtain users an subscribers'''
import requests


def number_of_subscribers(subreddit):
    '''Query in the API reddit an return the number of subscribers'''
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-agent': 'Chrome/85.0.4183.102'}
    query = requests.get(url, headers=headers)
    if query.status_code == 200:
        return(query.json()['data']['subscribers'])
    return (0)
