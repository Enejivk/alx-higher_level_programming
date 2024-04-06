#!/usr/bin/python3
"""
POSTING A VALUE TO THE SERVER
"""
import requests
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    email = argv[2]
    payload = {'email': email}
    r = requests.post(url, data=payload)
    print(r.text)
