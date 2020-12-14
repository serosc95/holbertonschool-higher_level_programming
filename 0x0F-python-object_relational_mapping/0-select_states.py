#!/usr/bin/python3
""" lists all states from the database """
import MySQLdb
from sys import argv


if __name__ == "__main__":
    user = argv[1]
    password = argv[2]
    datab = argv[3]
    conexion = MySQLdb.connect(host="localhost", port=3306, user=user,
                               passwd=password, db=datab, charset="utf8")
    cur = conexion.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
