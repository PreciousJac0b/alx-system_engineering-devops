#!/usr/bin/python3

"""
    This script fetches data fr0m a REST API and calculates
    the number of todos of a particular employee
"""

import json
import requests
import sys


def fetch_data(emp_id):
    """Handles both fetching and printing the data"""
    api_url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(api_url)
    response = response.json()
    total_num_of_tasks = 0
    total_num_of_done_tasks = 0
    task_title = ""
    for elem in response:
        if elem["userId"] == emp_id:
            total_num_of_tasks += 1
            if elem["completed"]:
                total_num_of_done_tasks += 1
                task_title += "     {}\n".format(elem["title"])

    user_url = "https://jsonplaceholder.typicode.com/users"
    user_response = requests.get(user_url)
    user_response = user_response.json()
    emp_name = ""

    for elem in user_response:
        if elem["id"] == emp_id:
            emp_name = elem["name"]

    print("Employee {} is done with tasks({}/{}):".format(
            emp_name, total_num_of_done_tasks, total_num_of_tasks))
    print("{}".format(task_title), end="")


if __name__ == '__main__':
    emp_id = int(sys.argv[1])
    fetch_data(emp_id)
