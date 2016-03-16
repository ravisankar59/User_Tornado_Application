from tornado import httpserver
from tornado import gen
from tornado.ioloop import IOLoop
import sqlite3 as sqlite
import tornado.web
import json
from config import execute


class AddUserHandler(tornado.web.RequestHandler):
    def get(self):
        query = '''SELECT * FROM person'''
        result = execute(query)
        print(result)
        
        self.write(json.dumps(dict(response=result)))

    def post(self):
        data = json.loads(self.request.body)
        fname = data.get('firstname')
        lname = data.get('lastname')
        phno = data.get('mobilenumber')
        address = data.get('address')
        query = ''' insert into person (firstname,lastname,mobilenumber,address) values ("{0}","{1}","{2}","{3}") '''.format(fname,lname,phno,address) ;
        result = execute(query)
        self.write(json.dumps(dict(response="Success")))

class SingleUserHandler(tornado.web.RequestHandler):

    def get(self, user_id):
        query = '''select * from person where id="{0}"'''.format(user_id);
        result = execute(query)
        if len(result) == 0:
            result = "User does not exist with the given ID {0}".format(user_id)

        self.write(json.dumps(dict(response=result)))

    def put(self, user_id):
        # print "In PUT"
        data = json.loads(self.request.body)
        uid = data.get('id')
        fname = data.get('firstname')
        lname = data.get('lastname')
        phno = data.get('mobilenumber')
        address = data.get('address')
        query = ''' update person set address="{1}" where id="{0}"'''.format(user_id,address);
        result = execute(query)
        print result
        self.write(json.dumps(dict(result="Success")))

    def delete(self, user_id):
        query = '''delete  from person where id = "{0}"'''.format(user_id);
        result = execute(query)
        self.write(json.dumps(dict(response=result)))
