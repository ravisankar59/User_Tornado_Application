from handlers import AddUserHandler, SingleUserHandler

url_patterns = [
            (r"/users" ,AddUserHandler),
            (r"/users/(?P<user_id>\w+)", SingleUserHandler)
        ]