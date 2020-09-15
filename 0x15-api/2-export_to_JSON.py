#!/usr/bin/python3
'''This script for obtain info about users in tha API'''

import json
import requests
from sys import argv


if __name__ == '__main__':
    URL = 'https://jsonplaceholder.typicode.com'
    todo = requests.get(URL + '/todos?userId=' + argv[1]).json()
    name = requests.get(URL + '/users/' + argv[1]).json()['username']
    new_dict = {}
    obj_j = {}
    new_list = []
    for item in todo:
        new_dict = {
            'task': item.get('title'),
            'completed': item.get('completed'),
            'username': name
        }
        new_list.append(new_dict)
    obj_j[argv[1]] = new_list
    with open('{}.json'.format(argv[1]), mode='w') as json_file:
        json.dump(obj_j, json_file)
