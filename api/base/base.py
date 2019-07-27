from .tools import underline_to_camel, camelize
import os
import json


class BaseClass(object):

    def __init__(self, *args):
        args = args[0]
        self.uri = args.get("uri"),
        self.uri = self.uri[0]
        self.headers = args.get("headers"),
        self.query_arguments = args.get("query_arguments", {})
        self.arguments = {}
        # for param in self.query_arguments:
        #     param = param.replace("'","/")
        #     json.loads(param)
        #     for k, v in param.items():
        #         self.arguments.update({k:v.decode("utf-8") })
        print(self.headers, self.query_arguments, self.uri)

