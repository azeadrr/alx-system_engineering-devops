#!/usr/bin/python3
"""this model is my firt time using REST API"""
import csv
import json
from sys import argv
from urllib import request


def to_csv(argv):
    tsks_id = request.urlopen(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(argv))
    user_name = request.urlopen(
        'https://jsonplaceholder.typicode.com/users/{}'.format(argv))
    res_body = tsks_id.read()
    user_body = user_name.read()
    json_dict = json.loads(res_body.decode("utf-8"))
    json_user = json.loads(user_body.decode("utf-8"))
    file_name = '{}.csv'.format(argv)
    with open(file_name, 'w') as csv_f:
        writer = csv.writer(csv_f, quoting=csv.QUOTE_ALL)

        for idx in range(0, len(json_dict)):
            writer.writerow([json_user['id'], json_user['username'],
                             json_dict[idx]['completed'],
                            json_dict[idx]['title']])
    csv_f.close()


if __name__ == "__main__":
    to_csv(argv=argv[1])
