#!/usr/bin/python3


import MySQLdb
from sys import argv


def main():
    """Lists all states from the database"""

db = MySQLdb.connect(
    host="localhost",
    port=3306,
    user=argv[1],
    passwd=argv[2],
    db=argv[3],
)
cursor = db.cursor()
cursor.execute("""SELECT * FROM states ORDER BY states.id ASC;""")
rows = cursor.fetchall()
for x in rows:
    print(x)
cursor.close()
db.close()

if __name__ == "__main__":
    main()
