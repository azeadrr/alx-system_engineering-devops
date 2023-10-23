#!/usr/bin/python3
"""this model is my firt time using REST API"""
import json
from sys import argv
from urllib import request


def get_user(argv):
    """this function do most of the job"""
    tsks_id = request.urlopen(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(argv))
    user_name = request.urlopen(
        'https://jsonplaceholder.typicode.com/users/{}'.format(argv))
    res_body = tsks_id.read()
    user_body = user_name.read()
    json_dict = json.loads(res_body.decode("utf-8"))
    json_user = json.loads(user_body.decode("utf-8"))
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
        get_user(argv=argv[1])
