from tornado import httpserver
from tornado import gen
from tornado.ioloop import IOLoop
import tornado.web
from urls import url_patterns
from config import UserDatabase

class Application(tornado.web.Application):
    def __init__(self):
        tornado.web.Application.__init__(self, url_patterns)

def main():

    # Verify the database exists and has the correct layout
    UserDatabase()

    app = Application()
    app.listen(8000)
    IOLoop.instance().start()

if __name__ == '__main__':
    main()