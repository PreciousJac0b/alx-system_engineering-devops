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
    tmp_array = []
    tmp_dict = {}

    for elem in user_response:
        if elem["id"] == emp_id:
            employee_name = elem["username"]

    api_url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(api_url)
    response = response.json()
    with open("{}.json".format(emp_id), "w+") as f:
        for elem in response:
            if elem["userId"] == emp_id:
                tmp_dict["task"] = elem["title"]
                tmp_dict["completed"] = elem["completed"]
                tmp_dict["username"] = employee_name
                tmp_array.append(tmp_dict)
                tmp_dict = {}
        return_dict = {}
        return_dict["{}".format(emp_id)] = tmp_array
        json.dump(return_dict, f)


if __name__ == '__main__':
    emp_id = int(sys.argv[1])
    fetch_data(emp_id)
