#!/usr/bin/python3
'''This script for obtain info about users in tha API'''
import csv
import requests
from sys import argv


if __name__ == '__main__':
    URL = 'https://jsonplaceholder.typicode.com'
    name = requests.get(URL + '/users/' + argv[1]).json()['name']
    todo = requests.get(URL + '/todos?userId=' + argv[1]).json()
    total_task = [(item) for item in todo]
    file = [
        total_task[int(argv[1])]['userId'],
        name,
        total_task[int(argv[1])]['completed'],
        total_task[int(argv[1])]['title']
    ]
    print(str(file[0]))
    with open('{}.csv'.format(argv[1]), mode='w') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        writer.writerow(file)
