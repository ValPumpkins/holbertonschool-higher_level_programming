#!/usr/bin/python3
""" Script that lists all cities from the database hbtn_0e_4_usa """

import MySQLdb
import sys

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    connection = MySQLdb.connect(host="localhost",
                                 port=3306,
                                 user=mysql_username,
                                 passwd=mysql_password,
                                 db=database_name
                                 )
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM cities ORDER BY id ASC")

    cities = cursor.fetchall()

    for city in cities:
        print(city)

    cursor.close()
    connection.close()
