# put db related methods here to share
import sqlite3


class DB(object):

    def __init__(self, pathToDb):
        self.pathToDb = pathToDb
        self.con = None
        self.cur = None

    def connect(self):
        if (self.con == None or self.cur == None):
            self.con = sqlite3.connect(self.pathToDb)
            self.cur = self.con.cursor()

    def disconnect(self):
        self.con.close()

    def execute(self, sql, params = False):
        self.connect()
        if (params != False):
            result = self.con.execute(sql, params)
        else:
            result = self.con.execute(sql)
        self.con.commit()
        return result

    def executeMany(self, sql, data):
        self.connect()
        result = self.con.executemany(sql, data)
        self.con.commit()
        return result

    def insert(self, sql, data):
        """
        a wrapper method return the the last row id
        """
        return self.execute(sql, data).lastrowid
