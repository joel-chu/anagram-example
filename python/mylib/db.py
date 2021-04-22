# put db related methods here to share
import sqlite3


class DB(object):

    def __init__(self, pathToDb):
        self.pathToDb = pathToDb
        self.con = None
        self.cur = None

    def connect():
        if (self.con == None || self.cur == None):
            self.con = sqlite3.connect(self.pathToDb)
            self.cur = self.con.cursor()

    def disconnect():
        self.con.close()

    def execute(sql, params = False):
        if (params != False):
            self.cur.execute(sql, params)
        else:
            self.cur.execute(sql)
        self.con.commit()

    def executeMany(sql, data):
        self.cur.executemany(insert_sql, data)
        self.con.commit()
