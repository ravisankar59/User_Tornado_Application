from tornado import httpserver
from tornado import gen
from tornado.ioloop import IOLoop
import sqlite3 as sqlite
import tornado.web

def execute(query):

        connection = sqlite.connect('User')
        cursorobj = connection.cursor()
        # print('EXECUTE ')
        try:
            cursorobj.execute(query)
            result = cursorobj.fetchall()
                # print(result)
            connection.commit()
        except Exception:
                        raise
        connection.close()
        return result


def UserDatabase():
    conn = sqlite.connect('User')
    c = conn.cursor()
    try:
        c.execute('SELECT * FROM person')
        # print(c.fetchall())
        print('Table already exists')
    except:
        # print("table does not exist")
        print('Creating table \'person\'')
        c.execute('CREATE TABLE person (\
            id integer primary key autoincrement,\
            firstname text,\
            lastname text,\
            mobilenumber text,\
            address text)')
        print('Successfully created table \'person\'')
    conn.commit()
    conn.close()
