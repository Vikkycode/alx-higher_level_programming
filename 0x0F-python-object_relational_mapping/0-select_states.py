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
    host = "localhost"
    user = sys.argv[1]
    pw = sys.argv[2]
    data = sys.argv[3]
    port = 3306
    db = MySQLdb.connect(host=host, user=user, passwd=pw, db=data, port=port)
    c = db.cursor()
    c.execute("SELECT * FROM states")
    result = c.fetchall()
    for state in result:
        print(state)
    c.close()
    db.close()
