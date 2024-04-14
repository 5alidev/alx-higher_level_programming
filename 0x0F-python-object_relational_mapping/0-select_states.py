#!/usr/bin/python3
# script that lists all states from the database hbtn_0e_0_usa
# usage: /0-select_states.py username password db_name
import MySQLdb
import sys

username = sys.argv[1]
password = sys.argv[2]
db_name = sys.argv[3]

if __name__ == "__main__":
    conn = MySQLdb.connect(
     host="localhost",
     port=3306,
     user=username,
     passwd=password,
     db=db_name,
     charset="utf8"
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
