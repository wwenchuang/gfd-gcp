"""
==========================
Author   : 文闯
Time     : 2022/07/28 11:05
FileName : path.py
Company  : 功夫豆
==========================
"""
import os

# 1、basedir
basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 拼到配置文件路径
conf_dir = os.path.join(basedir, "Conf")

# 拼接  测试数据路径
testdata_dir = os.path.join(basedir, "testdatas")

# 日志路径
log_dir = os.path.join(basedir, "output", "logs")

# 报告路径
report_dir = os.path.join(basedir, "outputs", "reports")