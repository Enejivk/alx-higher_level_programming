#!/usr/bin/python3
"""Script that returns a database based on the argument"""

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
    query = """ SELECT * FROM states 
            WHERE name LIKE "{}" 
            ORDER BY id ASC """.format(argv[4])
    
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
