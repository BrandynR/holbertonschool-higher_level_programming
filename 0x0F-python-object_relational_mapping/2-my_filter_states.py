#!/usr/bin/python3
"""
Displays all values in the states table of hbtn_0e_0_usa
where name matches the argument
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY \
    id ASC".format(sys.argv[4]))
    row = cursor.fetchall()
    for x in row:
        if x[1] == sys.argv[4]:
            print("({}, \'{}\')".format(x[0], x[1]))
    cursor.close()
    db.close()
