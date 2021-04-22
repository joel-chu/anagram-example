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
        if (params != False):
            result = self.cur.execute(sql, params)
        else:
            result = self.cur.execute(sql)
        self.con.commit()
        return result

    def executeMany(self, sql, data):
        result = self.cur.executemany(sql, data)
        self.con.commit()
        return result
