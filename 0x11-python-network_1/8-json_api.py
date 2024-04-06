#!/usr/bin/python3
"""
Posting a letter to an API
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    if len(argv) < 2:
        print("Usage: python script.py [letter]")
        exit(1)

    letter = argv[1]
    payload = {'q': letter}
    
    try:
        r = requests.post('http://localhost:5000/search_user', data=payload)
        r.raise_for_status()  # Raise an error for bad status codes
        jsonRep = r.json()
        if jsonRep:
            print("[{}] {}".format(jsonRep.get("name"), jsonRep.get("id")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
    except Exception as e:
        print("Error:", e)
