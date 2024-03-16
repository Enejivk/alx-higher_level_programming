#!/usr/bin/python3
"""This python connect to the database and list
content of hbtn_0e_0_usa database"""
import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost',
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306
                         )
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    items = cur.fetchall()
    for item in items:
        print(item)
    cur.close()
    db.close()
