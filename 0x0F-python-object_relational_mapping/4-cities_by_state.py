#!/usr/bin/python3
"""
Script to list all states from the database hbtn_0e_0_usa.

This script connects to a MySQL server running on localhost at port 3306
and retrieves all states from the database hbtn_0e_0_usa. The results are
sorted in ascending order by states.id and displayed.

Usage: ./list_states.py <username> <password> <database>

Arguments:
    username: MySQL username
    password: MySQL password
    database: MySQL database name

Example:
    ./list_states.py root root hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT c.id, c.name, s.name \
            FROM cities as c INNER JOIN  \
            states as s ON c.state_id = s.id \
            ORDER BY c.id ASC")
    cities = c.fetchall()
    [print(city) for city in cities]
