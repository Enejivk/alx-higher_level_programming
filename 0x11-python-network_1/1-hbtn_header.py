#!/usr/bin/python3
"""
printing the value of X-Request-Id
"""
import urllib.request
from sys import argv
with urllib.request.urlopen(argv[1]) as response:
    header = response.info()
    print(header['X-Request-Id'])
