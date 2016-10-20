# -*- coding: utf-8 -*-
import sqlite3


def InitializeDB(db):
    cur = db.cursor()
    sqlstatement = "CREATE TABLE STELLE("
    sqlstatement += "ID INT PRIMARY KEY NOT NULL, "
    sqlstatement += "Nome TEXT NOT NULL, "
    sqlstatement += "Designazione TEXT, "
    sqlstatement += "LumMin REAL, "
    sqlstatement += "LumMax REAL "
    sqlstatement += ");"
    cur.execute(sqlstatement)
    sqlstatement = "CREATE TABLE Campagne("
    sqlstatement += "ID INT PRIMARY KEY NOT NULL, "
    sqlstatement += "Nome TEXT NOT NULL, "
    sqlstatement += "Stella INT NOT NULL, "
    sqlstatement += "Periodo TEXT NOT NULL, "
    sqlstatement += "FOREIGN KEY(Stella) REFERENCES STELLE(ID)"
    sqlstatement += ");"
    cur.execute(sqlstatement)
    sqlstatement = "CREATE TABLE Osservazioni("
    sqlstatement += "ID INT PRIMARY KEY NOT NULL, "
    sqlstatement += "Campagna INT NOT NULL, "
    sqlstatement += "Stella INT NOT NULL, "
    sqlstatement += "Luogo TEXT NOT NULL, "
    sqlstatement += "Strumento TEXT NOT NULL, "
    sqlstatement += "Seeing INT NOT NULL, "
    sqlstatement += "Data TEXT NOT NULL, "
    sqlstatement += "Misura REAL NOT NULL, "
    sqlstatement += "StellaRif1 REAL NOT NULL, "
    sqlstatement += "StellaRif2 REAL, "
    sqlstatement += "Metodo TEXT NOT NULL, "
    sqlstatement += "Note TEXT NOT NULL, "
    sqlstatement += "FOREIGN KEY(Campagna) REFERENCES Campagne(ID), "
    sqlstatement += "FOREIGN KEY(Stella) REFERENCES STELLE(ID)"
    sqlstatement += ");"
    cur.execute(sqlstatement)


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
