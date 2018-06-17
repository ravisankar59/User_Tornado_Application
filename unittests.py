# test_async.py
import json
import unittest,urllib
from tornado.concurrent import Future
from tornado.web import HTTPError
from tornado.web import Application
from tornado.testing import gen_test
from mock import patch
from tornado.testing import AsyncHTTPTestCase
from handlers import AddUserHandler,SingleUserHandler

#  

class TestAddUsersHandler(AsyncHTTPTestCase):

    request_headers = {"content-type": "application/json"}
    route = "/users"

    def get_app(self):
        return Application([('/users', AddUserHandler)])

    @patch('handlers.get_all')
    def test_get_foo(self, get_all):
        result = [{"lastname": "afjal", "address": "None", "id": 2, "firstname": "None", "mobilenumber": "None"}, {"lastname": "jinu", "address": "abcd", "id": 4, "firstname": "rack", "mobilenumber": "9902771212111"}]
        get_all.return_value = result
        response = self.fetch(self.route)
        self.assertEquals(response.code, 200)
        response = json.loads(response.body.decode('utf-8'))
        self.assertEquals(len(response['users']),len(result))
        self.assertEquals(response['users'],result)

    @patch('handlers.create')
    def test_post_call(self, create):
        result = {"lastname": "mamidi", "address": "bangalore", "firstname": "ravisankar", "mobilenumber": "8722590390"}
        
        create.return_value = True
        response = self.fetch(self.route, method = "POST", body = json.dumps(result),
                            headers=self.request_headers)
        self.assertEquals(response.code, 200)
        response = json.loads(response.body.decode('utf-8'))
        expected_message = "successfully added user:{0} {1}".format(result["firstname"], result["lastname"])
        self.assertEquals(response["message"], expected_message)




class TestSingleUserHandler(AsyncHTTPTestCase):

    request_headers = {"content-type": "application/json"}
    route = "/users/{0}"

    def get_app(self):
        return Application([((r"/users/(?P<user_id>\w+)"), SingleUserHandler)])

    @patch('handlers.get_one')
    def test_get_user_call(self, get_one):
        result = {"lastname": "afjal", "address": "None", "firstname": "None", "mobilenumber": "None", "user_id": 2}
        # when user exists
        get_one.return_value = result
        user_id = 2
        route = self.route.format(user_id)
        response = self.fetch(route)
        self.assertEquals(response.code, 200)
        response = json.loads(response.body.decode('utf-8'))
        self.assertEquals(response, result)
        # when user does not exists
        get_one.return_value = None
        response = self.fetch(route)
        self.assertEquals(response.code, 404)

    @patch('handlers.create')
    def test_get_put_call(self, create):
        result = {"lastname": "mamidi", "address": "bangalore", "firstname": "ravisankar", "mobilenumber": "8722590390"}
        create.return_value = True
        user_id = 2
        route = self.route.format(user_id)
        response = self.fetch(route, method = "PUT", body = json.dumps(result),headers=self.request_headers)
        self.assertEquals(response.code, 200)
        response = json.loads(response.body.decode('utf-8'))
        expected_message = "Success"
        self.assertEquals(response["result"], expected_message)

    @patch('handlers.create')
    def test_get_DELETE_call(self, create):
        result = {"lastname": "mamidi", "address": "bangalore", "firstname": "ravisankar", "mobilenumber": "8722590390"}
        create.return_value = True
        user_id = 2
        route = self.route.format(user_id)
        response = self.fetch(route, method = "DELETE", headers=self.request_headers)
        self.assertEquals(response.code, 200)
        response = json.loads(response.body.decode('utf-8'))
        expected_message = "Successfully deleted user with id: {0}".format(user_id)
        self.assertEquals(response["message"], expected_message)








    




        
        
if __name__ == '__main__':
    unittest.main()



