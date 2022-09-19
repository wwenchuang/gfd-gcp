"""
==========================
Author   : 文闯
Time     : 2022/07/28 10:25
FileName : handle_phone.py
Company  : 功夫豆
==========================
"""
from faker import Faker
from common.mysql import Mysql


def get_new_phone():
    """
    # 得到没有注册过的手机号码。
    # 1、使用faker生成手机号码
    # 2、调用mysql数据库操作，去判断是否在数据中存在。如果不在，表示没有注册
    :return:
    """
    while True:
        phone = Faker("zh_CN").phone_number()
        sql = "select id from users where phone='{}'".format(phone)
        print(sql)
        res = Mysql().get_count(sql)
        print(res)
        print(phone)
        if res == 0:
            return phone
def is_exist_phone(phone):
    """
    # 得到没有注册过的手机号码。
    # 1、使用faker生成手机号码
    # 2、调用mysql数据库操作，去判断是否在数据中存在。如果不在，表示没有注册
    :return:
    """
    sql = "select id from users where phone='{}'".format(phone)
    res = Mysql().get_count(sql)
    if res == 0:
        return False
    else:
        return True