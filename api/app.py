import os
import sys
import tornado.web
import tornado.ioloop
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(BASE_DIR, 'api'))
from resources import ChatBot

 
application = tornado.web.Application([
    (r'/app/chat_bot', ChatBot),
])
 
if __name__ == "__main__":
    application.listen(8080)
    tornado.ioloop.IOLoop.instance().start()
