#!/usr/bin/python3
"""
Checking an error that is greater than 400
"""

from sys import argv
import requests

if __name__ == "__main__":
    url = argv[2]
    r = requests(url)
    statusCode = r.status_code

    if statusCode >= 400:
        print("Error code: {}".format(statusCode))
    else:
        print(r.text)
