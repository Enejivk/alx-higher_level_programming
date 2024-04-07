#!/usr/bin/python3

"""
Python script that get github ID from github API
"""

import requests
from requests.auth import HTTPBasicAuth
from sys import argv

if __name__ == "__main__":
    user_name = argv[1]
    password = argv[2]
    basic = HTTPBasicAuth(user_name, password)
    url = "https://api.github.com/users/{}".format(user_name)
    request = requests.get(url, auth=basic)
    print(request.json().get('id'))
