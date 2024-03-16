#!/usr/bin/python3
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', 
                         user='secroot', 
                         passwd='secroot', 
                         db='hbtn_0e_0_usa',
                         port=3306
                         )
    cur = db.cursor()
    cur.execute("SELECT id, name FROM states")
    for items in cur:
        print(items)
        