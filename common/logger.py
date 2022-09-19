"""
==========================
Author   : 文闯
Time     : 2022/07/28 15:44
FileName : logger.py
Company  : 功夫豆
==========================
"""
"""
1、设置日志的收集级别
2、可以将日志输出到文件和控制台

3、以下这些方法：
   info()
   debug()
   error()
   warning()
   critical()

额外拓展：单例模式
"""
import logging
from logging import Logger
import time
import os
from common import path
from common.conf import MyConf
from common.path import conf_dir


class MyLogger(Logger):

    def __init__(self):
        conf = MyConf(os.path.join(conf_dir, "conf.ini"))
        # file = conf.get("log", "file")
        # file = "api.log"
        file = os.path.join(path.log_dir, "{}.log".format(time.strftime('%Y%m%d%H%M', time.localtime(time.time()))))
        # 1、设置日志的名字、日志的收集级别
        super().__init__(conf.get("log","name"), conf.get("log","level"))
        # super().__init__("小白学习测试", logging.INFO)

        # 2、可以将日志输出到文件和控制台

        # 自定义日志格式(Formatter)
        fmt_str = "%(asctime)s %(name)s %(levelname)s %(filename)s [%(lineno)d] %(message)s"
        # 实例化一个日志格式类
        formatter = logging.Formatter(fmt_str)

        # 实例化渠道(Handle).
        # 控制台(StreamHandle)
        handle1 = logging.StreamHandler()
        # 设置渠道当中的日志显示格式
        handle1.setFormatter(formatter)
        # 将渠道与日志收集器绑定起来
        self.addHandler(handle1)

        if file:
            # 文件渠道(FileHandle)
            handle2 = logging.FileHandler(file, encoding="utf-8")
            # 设置渠道当中的日志显示格式
            handle2.setFormatter(formatter)
            self.addHandler(handle2)


logger = MyLogger()