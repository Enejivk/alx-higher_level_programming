#!/usr/bin/python3
"""
Getting the status of a website using request
"""
if __name__ == '__main__':
    import requests
    r = requests.get('https://alx-intranet.hbtn.io/status')
    body = r.text
    print('Body response:')
    print('\t- type: {}'.format(type(body)))
    print('\t- content: {}'.format(body))
