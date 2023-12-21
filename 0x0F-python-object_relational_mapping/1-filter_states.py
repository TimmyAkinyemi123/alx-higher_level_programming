#!/usr/bin/python3
""" lists all states with a name starting with N (upper N)
 from the database hbtn_0e_0_usa"""
from sys import argv
from unicodedata import name
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states` ORDER BY `id`")
    [print(state) for state in c.fetchall() if state[1][0] == "N"]
