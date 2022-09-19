"""
 -*- coding: utf-8 -*-
 @Time    : 2022/8/15 15:15
 @Author  : 文闯
 @File    : test_gcp.py
 @Software: PyCharm
 @company : 功夫豆信息科技
"""
import pytest
import os
import json

from common.conf import MyConf
from common.path import conf_dir
from common.request import MyRequests
from common.excel import MyExcel
from common.myassert import MyAssert
from common.logger import logger
from common.path import testdata_dir
from common.global_data import Data
from common.extract import extract_data_from_response
from common.replace import replace_case_with_re

# 第一步：读取注册接口的测试数据 - 是个列表，列表中的每个成员，都是一个接口用例的数据。
excel_path = os.path.join(testdata_dir, "../testdatas/gcp.xlsx")
print(excel_path)
me = MyExcel(excel_path, "gcp")
cases = me.read_data()

# 第二步：遍历测试数据，每一组数据，发起一个http的接口
# 实例化请求对象
mq = MyRequests()
massert = MyAssert()
class TestGcp:
    @pytest.mark.parametrize("case",cases)
    def test_gcp(self, case):
        # share_data = class_init
        # # 1、下一接口的请求数据中，需要替换，替换为上一个接口中提取的数据。
        # case = replace_case_with_re(case, share_data)
        #
        # 2、把替换之后的请求数据(json格式的字符串)，转换成一个字典
        req_dict = json.loads(case["req_data"])
        # 3、发起请求，并接收响应结果
        if hasattr(Data, "token"):
            resp = mq.send_requests(case["method"], case["url"], data=req_dict, token=getattr(Data, "token"))
        else:
            resp = mq.send_requests(case["method"], case["url"], data=req_dict)
        logger.info(resp.json())

        # 结果空列表
        assert_res = []

        # 5、断言响应结果中的数据
        if case["assert_list"]:
            response_check_res = massert.assert_response_value(case["assert_list"], resp.json())
            assert_res.append(response_check_res)

        if False in assert_res:
            pass
        else:
            # 4、提取响应结果中的数据,并设置为全局变量
            if case["extract"]:
                # 调用提取处理函数
                extract_data_from_response(case["extract"], resp.json(), share_data)

        # 6、断言数据库 - sql语句、结果与实际、比对的类型
        if case["assert_db"]:
            db_check_res = massert.assert_db(case["assert_db"])
            assert_res.append(db_check_res)

        # 最终的抛AsserttionError
        if False in assert_res:
            raise AssertionError

