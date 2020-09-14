# config.py

import gevent.monkey
gevent.monkey.patch_all()

import multiprocessing

debug = True
loglevel = 'debug'
bind = "0.0.0.0:5000"
pidfile = "logs/gunicorn.pid"
accesslog = "logs/access.log"
errorlog = "logs/debug.log"
# daemon = True

# 启动的进程数
workers = multiprocessing.cpu_count() * 2 + 1
# workers = 2
worker_class = 'thriftpy_gevent'
# x_forwarded_for_header = 'X-FORWARDED-FOR'

thrift_protocol_factory = "thriftpy2.protocol:TCompactProtocolFactory"  # 客户端生成的时候要和这个对应，传输协议， 高效率的、密集的二进制编码格式进行数据传输，推荐使用
thrift_transport_factory = "thriftpy2.transport:TBufferedTransportFactory"  # 加了缓存的传输控制，推荐方式
