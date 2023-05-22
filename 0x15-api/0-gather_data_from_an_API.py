#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import requests
from sys import argv


if __name__ == '__main__':
    employeeId = argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + employeeId

    res = requests.get(url)
    employeeName = res.json().get('name')

    todoUrl = url + "/todos"
    res = requests.get(todoUrl)
    tasks = res.json()
    done = 0
    done_tasks = []

    for task in tasks:
        if task['completed']:
            done_tasks.append(task)
            done += 1

    print("Emplyee {employeeName} is done with tasks({done}/{}):".format(len(tasks)))

    for task in done_tasks:
        print("\t {}".format(task.get('title')))
