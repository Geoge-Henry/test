import os
import sys
import tornado.web
import tornado.ioloop
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(BASE_DIR, 'api'))
from resources import ChatBot

settings = {'debug': True}

application = tornado.web.Application([
    (r'/app/chat_bot', ChatBot),
], **settings)
 
if __name__ == "__main__":
    application.listen(5000)
    tornado.ioloop.IOLoop.instance().start()
