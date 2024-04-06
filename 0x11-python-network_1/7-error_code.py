#!/usr/bin/python3
"""
Checking an error that is greater than 400
"""
from sys import argv
import requests

if __name__ == "__main__":
    url = argv[1]
    r = requests.get(url)
    statusCode = r.status_code
    if statusCode >= 400:
        print("Error code: {}".format(statusCode))
    else:
        print(r.text)
