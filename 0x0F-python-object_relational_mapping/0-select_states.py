#!/usr/bin/python3
import MySQLdb

"""This python connect to the database and list
content of hbtn_0e_0_usa database"""

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost',
                         user='secroot',
                         passwd='secroot',
                         db='hbtn_0e_0_usa',
                         port=3306
                         )
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    items = cur.fetchall()
    for item in items:
        print(item)
    cur.close()
    db.close()