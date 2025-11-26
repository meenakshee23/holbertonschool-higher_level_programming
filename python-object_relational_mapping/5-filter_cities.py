#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists all 
cities of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: ./5-filter_cities.py <user> <password> <database> <state_name>")
        sys.exit(1)

    user, password, db_name, state_name = sys.argv[1:5]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=user, passwd=password, db=db_name)
    cursor = db.cursor()

    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))

    cities = [row[0] for row in cursor.fetchall()]
    print(", ".join(cities))

    cursor.close()
    db.close()
