#!/usr/bin/python3
""" Python script that
using this REST AP"""
import json
from sys import argv
from urllib import request

def usr(argv):
    """Gather data from an API"""
    tasksid = request.urlopen(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(argv))
    userid = request.urlopen(
        'https://jsonplaceholder.typicode.com/users/{}'.format(argv))
    res = tasksid.read()
    user = userid.read()
    json_dict = json.loads(res.decode("utf-8"))
    json_user = json.loads(user.decode("utf-8"))
    count = 0
    for i in range(0, len(json_dict)):
        if not json_dict[i]['completed']:
            count += 1
            print('Employee {} is done with tasks({}/{}):'
          .format(json_user['name'], len(json_dict) - count, len(json_dict)))
    for idx in range(0, len(json_dict)):
        if json_dict[idx]['completed']:
            print('\t {}'.format(json_dict[idx]['title']))


if __name__ == "__main__":
    if len(argv) == 2:
        usr(argv=argv[1])
