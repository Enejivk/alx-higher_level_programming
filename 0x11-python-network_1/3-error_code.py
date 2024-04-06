#!/usr/bin/python3
"""
Python script to send a request to a URL and display the body of the response.
"""

import urllib.request
import sys
from urllib.error import HTTPError

if __name__ == "__main__":
    url = sys.argv[1]
    
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except HTTPError as e:    
        print('Error code: {}'.format(e.code))
