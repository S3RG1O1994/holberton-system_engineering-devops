#!/usr/bin/python3
'''Function for obtain users an subscribers'''
import requests


def recurse(subreddit, hot_list=[], after=''):
    '''Query in the API reddit an return the number of subscribers'''
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
        subreddit, after)
    headers = {'User-agent': 'Chrome/85.0.4183.102'}
    query = requests.get(url, headers=headers, allow_redirects=False)
    if query.status_code == 200:
        file = query.json().get('data')
        after = file.get('after')
        other_file = file.get('children')
        # print(other_file[len(other_file) - 1]['data']['title'])
        if after:
            # other_file = other_file[len(other_file) - 1]
            [hot_list.append(i.get('data').get('title')) for i in other_file]
            return recurse(subreddit, hot_list, after)
        elif len(hot_list) == 0:
            return None
        else:
            return hot_list
    else:
        return None
