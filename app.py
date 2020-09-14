# _*_coding:utf-8_*_
# __author: g
import os

import thriftpy2
from thriftpy2.thrift import TProcessor

tp = thriftpy2.load(os.path.join(os.path.dirname(__file__), "hello.thrift"))

service = tp.TestService  # *.thrift文件的 server名


class TestServer:
    def hello(self, msg):
        # time.sleep(2)
        return f"{msg}, hello"


app = TProcessor(tp.TestService, TestServer())
