# python gunicorn_thrift
## 本地安装 thrift，gunicorn_thrift

> python3 -m venv env  生成python虚拟环境

> source env/bin/activate  进入虚拟环境

> pip install -r requirements.txt  安装py包

> mkdir thrift_sdk  创建生成rpc代码的目录

> mkdir logs  创建gunicorn所需要日志文件

> thrift --out thrift_sdk --gen py hello.thrift  生成rpc文件
 
> gunicorn_thrift -c deploy/gunicorn/gunicorn_config.py app:app  启动应用，具体配置见deploy/gunicorn/gunicorn_config.py
