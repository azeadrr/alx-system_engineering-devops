#!/usr/bin/python3
"""Dictionary of list of dictionaries"""
import json
from sys import argv
from urllib import request


def expo_to_json():
    """extend your Python script to export data in the JSON format"""
    tasks_id = request.urlopen(
        'https://jsonplaceholder.typicode.com/todos/')
    usr_name = request.urlopen(
        'https://jsonplaceholder.typicode.com/users/')
    res_body = tasks_id.read()
    user_body = usr_name.read()
    json_dict = json.loads(res_body.decode("utf-8"))
    json_user = json.loads(user_body.decode("utf-8"))

    file_name = 'todo_all_employees.json'
    usr_task = {}
    for idx in range(0, len(json_user)):
        liste = []
        for jdx in range(0, len(json_dict)):
            task_dict = {}
            if json_dict[jdx]['userId'] == json_user[idx]['id']:
                task_dict['username'] = json_user[idx]['username']
                task_dict['task'] = json_dict[jdx]['title']
                task_dict['completed'] = json_dict[jdx]['completed']
                liste.append(task_dict)
        usr_task[json_user[idx]['id']] = liste

    object_json = json.dumps(usr_task, indent=4)

    with open(file_name, 'w') as json_f:
        json_f.write(object_json)
    json_f.close()


if __name__ == "__main__":
    expo_to_json()
