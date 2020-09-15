#!/usr/bin/python3
'''This script for obtain info about users in tha API'''

import json
import requests
from sys import argv


if __name__ == '__main__':
    URL = 'https://jsonplaceholder.typicode.com'
    name = requests.get(URL + '/users/').json()
    new_dict = {}
    obj_j = {}
    new_list = []
    for user in name:
        un = user.get('username')
        UID = user.get('id')
        todo = requests.get(URL + '/todos?userId={}'.format(UID)).json()
        for item in todo:
            new_dict = {
                'username': un,
                'task': item.get('title'),
                'completed': item.get('completed'),
            }
            new_list.append(new_dict)
        obj_j[UID] = new_list
    with open('todo_all_employees.json', mode='w') as json_file:
        json.dump(obj_j, json_file)
