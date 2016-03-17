from tornado import httpserver
from tornado import gen
from tornado.ioloop import IOLoop
import sqlite3 as sqlite
import tornado.web
import json
from config import get_all,get_one, create


class AddUserHandler(tornado.web.RequestHandler):
    def get(self):
        query = '''SELECT * FROM person'''
        result = get_all(query)
        self.write(json.dumps(dict(users=result)))

    def post(self):
        data = json.loads(self.request.body)
        fname = data.get('firstname')
        lname = data.get('lastname')
        phno = data.get('mobilenumber')
        address = data.get('address')
        query = ''' INSERT INTO person (firstname,lastname,mobilenumber,address) VALUES ("{0}","{1}","{2}","{3}") '''.format(fname,lname,phno,address) ;
        result = create(query)
        self.write(json.dumps(dict(message="successfully added user:{0} {1}".format(fname, lname))))

class SingleUserHandler(tornado.web.RequestHandler):

    def get(self, user_id):
        query = '''SELECT * FROM person WHERE id="{0}"'''.format(user_id);
        result = get_one(query)
        if result is None:
            result = "User does not exist with the ID: {0}".format(user_id)

        self.write(json.dumps(result))

    def put(self, user_id):
        params = json.loads(self.request.body)
        query_params = ",".join('''"{0}"="{1}"'''.format(key, params[key]) for key in params if params[key]is not None)
        query = ''' UPDATE person SET {0} WHERE id="{1}"'''.format(query_params,user_id);
        result = create(query)
        self.write(json.dumps(dict(result="Success")))

    def delete(self, user_id):
        query = '''DELETE FROM person WHERE id = "{0}"'''.format(user_id);
        result = create(query)
        self.write(json.dumps(dict(message="Successfully deleted user with id: {0}".format(user_id))))
