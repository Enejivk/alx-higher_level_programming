#!/usr/bin/python3
"""
Posting a letter to an API
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    if argv[1]:
        letter = argv[1]
    else:
        letter = ""
    payload = {'q': letter}
    r = requests.post('http://0.0.0.0:5000/search_user', data=payload)
    try:
        jsonRep = r.json()
        if jsonRep == {}:
            print("No result")
        else:
            print("[{}] {}".format(jsonRep.get("name"), jsonRep.get("id")))
    except ValueError:
        print("Not a valid JSON")    
