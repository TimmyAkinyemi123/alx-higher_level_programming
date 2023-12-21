#!/usr/bin/python3
"""
displays all values in the states table of 
hbtn_0e_0_usa where name matches the argument"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    c = db.cursor()
    c.execute("""SELECT * FROM states""")
    [print(state) for state in c.fetchall() if state[1] == argv[4]]
