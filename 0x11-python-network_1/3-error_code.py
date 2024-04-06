#!/usr/bin/python3
"""
checking for http error
"""
if __name__ == "__main__":
    import urllib.request
    from sys import argv
    from urllib.error import HTTPError
    url = argv[1]
    
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('ascii')
            print(body)
    except HTTPError as e:    
        print('Error code: {}'.format(e.code))
