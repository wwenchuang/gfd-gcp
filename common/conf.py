"""
==========================
Author   : 文闯
Time     : 2022/07/28 10:50
FileName : conf.py
Company  : 功夫豆
==========================
"""
from configparser import ConfigParser

class MyConf(ConfigParser):
    def __init__(self,filename):
        super().__init__()
        self.read(filename,encoding="utf-8")