#!/usr/bin/python3
"""
get data from API, retrieving TODO list data
given employee ID
export result to JSON
"""

import json
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
    all_tasks = []
    data = {str(id): all_tasks}
    for todo in todo_json:
        if todo.get('userId') == id:
            task_dict = {
                "task": todo.get('title'),
                "completed": todo.get('completed'),
                "username": name
            }
            all_tasks.append(task_dict)

            if todo.get('userId') != id:
                break

    # write to csv
    with open('USER_ID.json', 'w') as file:
        json.dump(data, file)
