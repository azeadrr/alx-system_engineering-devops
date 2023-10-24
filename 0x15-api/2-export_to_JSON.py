#!/usr/bin/python3
"""Python script to export data in the JSON format"""
import json
from sys import argv
from urllib import request


def expo_to_json(argv):
    """ Export to JSON"""
    tasks_id = request.urlopen(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(argv))
    usr_name = request.urlopen(
        'https://jsonplaceholder.typicode.com/users/{}'.format(argv))
    res_body = tasks_id.read()
    user_body = usr_name.read()
    json_dict = json.loads(res_body.decode("utf-8"))
    json_user = json.loads(user_body.decode("utf-8"))

    file_name = '{}.json'.format(argv)
    liste = []
    for idx in range(0, len(json_dict)):
        tsk_dict = {}
        tsk_dict['task'] = json_dict[idx]['title']
        tsk_dict['completed'] = json_dict[idx]['completed']
        tsk_dict['username'] = json_user['username']
        liste.append(tsk_dict)

    usr_task = {}
    usr_task[json_user['id']] = liste
    object_json = json.dumps(usr_task, indent=4)
    with open(file_name, 'w') as json_f:
        json_f.write(object_json)
    json_f.close()


if __name__ == "__main__":
    if len(argv) == 2:
        expo_to_json(argv=argv[1])
