#!/usr/bin/python3
""" Python script that
using this REST AP"""
import json
from sys import argv
from urllib import request


def get_user(argv):
    """Gather data from an API"""
    tasksid = request.urlopen(
            'https://jsonplaceholder.typicode.com/todos?userId={}'.format(argv))
    userid = request.urlopen(
            'https://jsonplaceholder.typicode.com/users/{}'.format(argv))
    res = tasksid.read()
    user = userid.read()
    json_dct = json.loads(res.decode("utf-8"))
    json_usr = json.loads(user.decode("utf-8"))
    count = 0
    for i in range(0, len(json_dct)):
        if not json_dct[i]['completed']:
            count += 1
    print('Employee {} is done with tasks({}/{}):'
          .format(json_usr['name'], len(json_dct) - count, len(json_dct)))
    for id in range(0, len(json_dct)):
        if json_dct[id]['completed']:
            print('\t {}'.format(json_dct[id]['title']))


if __name__ == "__main__":
    if len(argv) == 2:
        get_user(argv=argv[1])
