__author__ = 'kvogelgesang'

from configuration import SetEnv
import sqlite3
import sys

class Database(object):

    cursor = None

    def __init__(self, db_name, caller, sql_dialect='sqlite',create_tables=False, in_memory=True):
        if not sql_dialect:
            sys.exit("No sql dialect given - exit!")
        self.sql_dialect = sql_dialect
        if not db_name and not in_memory:
            sys.exit("No database name given - exit!")
        if in_memory:
            self.db_name = ":memory:"
        else:
            self.db_name = db_name
        self.db_in_memory = in_memory
        print "Init database with name: %s, dialect: %s, in_memory: %s, called from: %s" % (self.db_name, self.sql_dialect, in_memory, caller)


    def connect_sqlite(self):
        self.connection = sqlite3.connect(self.db_name)
        return self.connection

    def close(db,self):
        db.cursor().close()
        db.close()

class Sql(object):

    database = None
    cursor = None
    auto_commit = True
    sql_dialect = None

    def __init__(self, database):
        self.database = database

    def get_all_cds(self):
        sql = "SELECT * FROM cds;"
        return self.database.cursor().execute(sql).fetchall()

    def get_cds_by_interpret(self,interpret):
        interpret = "%" + interpret + "%"
        sql = "SELECT * FROM cds WHERE interpret LIKE '%s';" % interpret
        return self.database.cursor().execute(sql).fetchall()


if __name__ == '__main__':
    db_name = SetEnv().resources_dir + "/cdcol.sqlite"
    db = Database(db_name, __name__, sql_dialect="sqlite", in_memory=False).connect_sqlite()
    #result = Sql(db).get_all_cds()
    result = Sql(db).get_cds_by_interpret("Van")
    print str(result[0][0])
    db.close()