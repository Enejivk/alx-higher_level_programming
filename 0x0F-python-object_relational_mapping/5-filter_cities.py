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
    query = """ SELECT cities.name
            FROM states
            JOIN cities
            ON states.id = cities.state_id
            WHERE states.name = %s
            ORDER BY cities.id ASC """

    cur.execute(query, (argv[4],))
    rows = cur.fetchall()
    tmp = list(row[0] for row in rows)
    print(*tmp, sep=", ")
    cur.close()
    db.close()
