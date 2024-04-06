#!/usr/bin/python3
"""
Getting the value of X-Request-Id from the header
"""
if __name__ == "__main__":
    from sys import argv
    import requests

    url = argv[1]
    r = requests.get(url)
    header = r.headers
    print(header.get('X-Request-Id'))
