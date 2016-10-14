# -*- coding: utf-8 -*-
import sqlite3


def InitializeDB(db):
    print("Work in Progress")


def TestDatabase():
    try:
        db = sqlite3.connect('test.db')
        cur = db.cursor()
        cur.execute("select count(*) from sqlite_master")
        if cur.fetchone() < (1, ):
            InitializeDB(db)
    except sqlite3.Error as e:
        print("Error %s: " % e.args[0])
        exit(1)
