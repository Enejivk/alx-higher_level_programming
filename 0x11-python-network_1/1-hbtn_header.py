#!/usr/bin/python3
"""
printing the value of X-Request-Id
"""
if __name__ == "__main__":
    import urllib.request
    from sys import argv
    with urllib.request.urlopen(argv[1]) as response:
        header = response.info()
        print("{}".format(header.get("X-Request-Id")))
