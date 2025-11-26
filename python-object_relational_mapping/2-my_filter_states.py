#!/usr/bin/python3
"""Script that takes in an argument
and displays all values in the states table of hbtn_0e_0_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    username, password, db_name, state_name = sys.argv[1:5]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=db_name)
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE LOWER(name) = LOWER(%s) ORDER BY id ASC",
        (state_name,)
    )

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
