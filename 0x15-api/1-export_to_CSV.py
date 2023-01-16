#!/usr/bin/python3

"""
    This script fetches data fr0m a REST API and calculates
    the number of todos of a particular employee
"""

import csv
import json
import requests
import sys


def fetch_data(emp_id):
    """Handles both fetching and printing the data"""
    user_url = "https://jsonplaceholder.typicode.com/users"
    user_response = requests.get(user_url)
    user_response = user_response.json()
    employee_name = ""
    tmp_string = []

    for elem in user_response:
        if elem["id"] == emp_id:
            employee_name = elem["name"]

    api_url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(api_url)
    response = response.json()
    total_num_of_tasks = 0
    total_num_of_done_tasks = 0
    task_title = ""
    with open("{}.csv".format(emp_id), "w+", newline="", encoding='utf-8') as f:
        writer = csv.writer(f)
        for elem in response:
            if elem["userId"] == emp_id:
                tmp_string = ["{}".format(elem["userId"]), "{}".format(employee_name),  "{}".format(elem["completed"]), "{}".format(elem["title"])]
                writer.writerow(tmp_string)
                tmp_string = []


if __name__ == '__main__':
    emp_id = int(sys.argv[1])
    fetch_data(emp_id)
