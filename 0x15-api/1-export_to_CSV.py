#!/usr/bin/python3
'''This script for obtain info about users in tha API'''
import csv
import requests
from sys import argv


if __name__ == '__main__':
    URL = 'https://jsonplaceholder.typicode.com'
    name = requests.get(URL + '/users/' + argv[1]).json()['username']
    todo = requests.get(URL + '/todos?userId=' + argv[1]).json()
    with open('{}.csv'.format(argv[1]), mode='w') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for item in todo:
            writer.writerow([int(argv[1]), name,
                item.get('completed'), item.get('title')])
