#!/usr/bin/python3
"""
posting a request to a server containing email
"""
import urllib.request
import urllib.parse
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    values = {'email': argv[2]}
    url_value = urllib.parse.urlencode(values)
    data = url_value.encode('utf-8')
    req = urllib.request.Request(url, data=data, method='POST')
    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')
        print(body)
