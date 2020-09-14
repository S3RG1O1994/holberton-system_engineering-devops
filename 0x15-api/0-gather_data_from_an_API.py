#!/usr/bin/python3
'''This script for obtain info about users in tha API'''

import requests
from sys import argv


if __name__ == '__main__':
    URL = 'https://jsonplaceholder.typicode.com'
    name = requests.get(URL + '/users/' + argv[1]).json()['name']
    todo = requests.get(URL + '/todos?userId=' + argv[1]).json()
    total_task = [(item) for item in todo]
    list_completed = [(item) for item in todo if item.get('completed') is True]
    print('{} is done with tasks({}/{})'.format(name, len(list_completed), len(total_task)))
    for i in list_completed:
        print('\t {}'.format(i['title']))
