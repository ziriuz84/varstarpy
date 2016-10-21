# -*- coding: utf-8 -*-


class Stella:
    def __init__(self):
        self.ID = 0
        self.Nome = ""
        self.Designazione = ""
        self.LumMin = 0.0
        self.LumMax = 0.0

    def Aggiungi(self, db):
        cur = db.cursor()
        sqlstatement = "SELECT COUNT(*) FROM STELLE"
        cur.execute(sqlstatement)
        self.ID = cur.fetchone()[0]
        sqlstatement = "INSERT INTO STELLE VALUES(?, ?, ?, ?, ?);"
        cur.execute(sqlstatement, (self.ID,
                                   self.Nome,
                                   self.Designazione,
                                   self.LumMin,
                                   self.LumMax))
        db.commit()
