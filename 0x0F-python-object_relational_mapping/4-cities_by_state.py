#!/usr/bin/python3
"""Using Join to return the state and the cities"""

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
    query = """ SELECT cities.id, cities.name, states.name
            FROM states
            JOIN cities
            ON states.id = cities.state_id
            ORDER BY cities.id ASC """

    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
