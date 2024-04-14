#!/usr/bin/python3
"""script that lists all states with a name starting with N"""
# Usage: ./1-filter_states.py username password db_name
import sys
import MySQLdb

if __name__ == "__main__":
    con = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                          passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = con.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%'")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    con.close()
