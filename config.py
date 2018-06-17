from tornado import httpserver
from tornado import gen
from tornado.ioloop import IOLoop
import sqlite3 as sqlite
import tornado.web

def dict_gen(query):
    print query
    connection = sqlite.connect('Users')
    cursorobj = connection.cursor()
    cursorobj.execute(query)
    print(dir(cursorobj))
    print(cursorobj.description)
    ''' From Python Essential Reference by David Beazley'''
    import itertools
    field_names = [d[0].lower() for d in cursorobj.description]
    while True:
        print cursorobj
        rows = cursorobj.fetchma()
        if not rows: return
        for row in rows:
            yield dict(itertools.izip(field_names, row))
    # connection.commit()
    # connection.close()

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def get_all(query):

        connection = sqlite.connect('Users')
        connection.row_factory = dict_factory
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

def get_one(query):

        connection = sqlite.connect('Users')
        connection.row_factory = dict_factory
        cursorobj = connection.cursor()
        # print('EXECUTE ')
        try:
            cursorobj.execute(query)
            result = cursorobj.fetchone()
                # print(result)
            connection.commit()
        except Exception:
                        raise
        connection.close()
        return result

def create(query):

        connection = sqlite.connect('Users')
        connection.row_factory = dict_factory
        cursorobj = connection.cursor()
        # print('EXECUTE ')
        try:
            cursorobj.execute(query)
            result = cursorobj.fetchone()
            # result = cursorobj.fetchone()
            #     # print(result)
            connection.commit()
        except Exception:
                        raise
        connection.close()
        return result



def UserDatabase():
    conn = sqlite.connect('Users')
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
