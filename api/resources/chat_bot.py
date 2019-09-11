import sys
sys.path.append("../")
from base import BaseClass


class ChatBot(BaseClass):
    # def __init__(self):
    #     print("ok")

    def get(self):
        print("okk")
        self.write("gggg")
        print(self.get_query_argument("asd"))
        print(222)

