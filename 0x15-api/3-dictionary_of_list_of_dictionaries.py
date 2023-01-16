#!/usr/bin/python3

"""
    This script fetches data fr0m a REST API and calculates
    the number of todos of a particular employee
"""

import csv
import json
import requests
import sys


def fetch_data():
    """Handles both fetching and printing the data"""
    user_url = "https://jsonplaceholder.typicode.com/users"
    user_response = requests.get(user_url)
    user_response = user_response.json()
    employee_name = ""
    tmp_array = []
    tmp_dict = {}
    return_dict = {}

    for elem in user_response:
        return_dict[elem["id"]] = []

    api_url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(api_url)
    response = response.json()
    with open("todo_all_employees.json", "w+") as f:
        for elem in response:
            for elems in user_response:
                if elems["id"] == elem["userId"]:
                    tmp_dict["username"] = elems["username"]
            tmp_dict["task"] = elem["title"]
            tmp_dict["completed"] = elem["completed"]
            return_dict[elem["userId"]].append(tmp_dict)
            # tmp_array.append(tmp_dict)
            tmp_dict = {}
        json.dump(return_dict, f)


if __name__ == '__main__':
    fetch_data()
