#!/usr/bin/python3
"""python script that execute Mysql query and return only character
starting with capital letter N"""


import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost',
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         port=3306
                         )
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name REGEXP '^N' ORDER BY id ASC")
    data = cur.fetchall()
    for item in data:
        print(item)
