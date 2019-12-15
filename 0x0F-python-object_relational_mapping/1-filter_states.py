#!/usr/bin/python3
"""
List all states with a name starting with N
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    rows = cursor.fetchall()
    for x in row:
        if x[1][0] == 'N':
            print("({}, \'{}\')".format(x[0], x[1]))
    cursor.close()
    db.close()
