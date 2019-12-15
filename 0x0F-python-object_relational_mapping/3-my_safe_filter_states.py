#!/usr/bin/python3
"""
test "Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '"
as an input from previous script
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
    cursor.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC",
                   (sys.argv[4],))
    row = cursor.fetchall()
    for x in row:
        print("({}, \'{}\')".format(x[0], x[1]))
    cursor.close()
    db.close()
