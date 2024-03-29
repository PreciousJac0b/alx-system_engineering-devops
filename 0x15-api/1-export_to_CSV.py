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
            employee_name = elem["username"]

    api_url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(api_url)
    response = response.json()
    total_num_of_tasks = 0
    total_num_of_done_tasks = 0
    task_title = ""
    with open("{}.csv".format(emp_id), "w+", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for elem in response:
            if elem["userId"] == emp_id:
                tmp_string = [str(elem.get("userId")),
                              str(employee_name),
                              str(elem.get("completed")),
                              str(elem.get("title"))]
                writer.writerow(tmp_string)
                tmp_string = []


if __name__ == '__main__':
    emp_id = int(sys.argv[1])
    fetch_data(emp_id)
