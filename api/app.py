import os
import sys
import tornado.web
import tornado.ioloop
from base import BaseClass
import importlib
BASE_PATH = os.path.dirname(os.path.dirname(__file__)) + "/api"
sys.path.append(BASE_PATH)
from base.tools import underline_to_camel, camelize, get_file_class_params


class IndexHandler(tornado.web.RequestHandler):
 
    def get(self, *args, **kwargs):
        base_params = dict(
            uri = self.request.uri,
            headers = self.request.headers,
            query_arguments = self.request.query_arguments,
        )
        file_path, class_name = get_file_class_params(base_params)
        module = importlib.import_module("resources." + file_path)
        class_name = getattr(module, class_name)
        class_obj = class_name()
        func = sys._getframe().f_code.co_name
        func = getattr(class_obj, func)
        func()
        # base_handle = BaseClass(base_params)
    
    def post(self, *args, **kwargs):
        self.write("Hello World, My name is 蔡智恒")
        print("Hello World, My name is 蔡智恒", args)

 
application = tornado.web.Application([
    (r'/app/(.*)',IndexHandler),
])
 
if __name__ == "__main__":
    application.listen(8080)
    tornado.ioloop.IOLoop.instance().start()