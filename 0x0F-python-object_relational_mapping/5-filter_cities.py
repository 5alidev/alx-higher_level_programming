#!/usr/bin/python3
""" script that lists all cities from the database hbtn_0e_4_usa """
# Usage: ./4-cities_by_state.py username password db_name
import sys
import MySQLdb


if __name__ == "__main__":
    state = sys.argv[4]
    con = MySQLdb.connect(host='localhost', port=3306,
                          user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = con.cursor()
    cur.execute("""SELECT c.name FROM cities c INNER JOIN
                   states s ON c.state_id = s.id WHERE s.name = %s
                   ORDER BY c.id ASC""", (state, ))
    query_rows = cur.fetchall()
    tmpList = list(row[0] for row in query_rows)
    print(*tmpList, sep=", ")
    cur.close()
    con.close()
