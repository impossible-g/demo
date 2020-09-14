# _*_coding:utf-8_*_
# __author: g
import os

import thriftpy2.rpc
from thriftpy2.protocol import TCompactProtocolFactory

if __name__ == '__main__':
    tp = thriftpy2.load(os.path.join(os.path.dirname(__file__), "hello.thrift"))

    cli = thriftpy2.rpc.make_client(tp.TestService, "localhost", 5000, proto_factory=TCompactProtocolFactory())

    ret = cli.hello("123")
    print(ret)
