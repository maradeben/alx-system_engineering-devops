#!/usr/bin/python3
"""
get data from API, retrieving TODO list progress
given employee ID
"""

import requests
from sys import argv


if __name__ == '__main__':

    # get user passed in as argument
    id = int(argv[1])

    # retrieve user data
    user_url = "https://jsonplaceholder.typicode.com/users"
    user_resp = requests.get(user_url)
    user_json = user_resp.json()
    user_dict = {}
    for user in user_json:
        user_dict[user['id']] = user.get('name')

    # retrieve todo data
    todo_url = "https://jsonplaceholder.typicode.com/todos"
    todo_resp = requests.get(todo_url)
    todo_json = todo_resp.json()

    # parse data
    name = user_dict[id]
    total_task = 0
    completed_tasks = 0
    completed_tasks_list = []
    for todo in todo_json:
        if todo.get('userId') == id:
            total_task += 1
            if todo.get('completed'):
                completed_tasks += 1
                completed_tasks_list.append(todo.get('title'))
            if todo.get('userId') != id:
                break

    print("Employee {} is done with tasks({}/{}):".format
          (name, completed_tasks, total_task))
    for task in completed_tasks_list:
        print("\t {}".format(task))
