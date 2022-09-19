"""
 -*- coding: utf-8 -*-
 @Time    : 2022/8/15 15:05
 @Author  : 文闯
 @File    : replace.py
 @Software: PyCharm
 @company : 功夫豆信息科技
"""
import re
from common.global_data import  Data
from common.logger import logger
from common.handle_phone import get_new_phone

"""
在编写测试用例时，用例涉及到的所有mark标识符(#...#)都能够替换成功

用来替换的数据：
1、来自响应结果当中提取
2、脚本生成的(phone)
3、配置文件..

请问在框架当中，Data类主要用在哪些地方？
1、封装的提取方法(从响应结果中提取数据放到Data中)
2、封装的替换方法(从Data当中拿数据)

"""

def replace_case_with_re(case_dict, share_data_obj:Data):
    """
    替换测试用例当中所有的标识符，通过正则表达式获取所有的mark，然后遍历mark一个个替换。
    替换的值呢，来自于：
    1、如果是#phone#，则来自于脚本生成。表示要一个未注册的手机号码
    2、其它的mark，均从Data类的属性中获取。

    :param case_dict: 从excel当中是读取出来的一行测试数据。为字典形式。
    :return: 替换之后的测试数据。类型为字典。
    """
    # 第一步，把excel当中的一整个测试用例(excel当中的一行)转换成字符串
    case_str = str(case_dict)

    # 第二步，利用正则表达式提取mark标识符
    to_be_replaced_marks_list = re.findall("#(\w+)#", case_str)

    # 第三步：遍历标识符mark，如果标识符是全局变量Data类的属性名，则用属性值替换掉mark
    if to_be_replaced_marks_list:
        logger.info("要替换的mark标示符有:{}".format(to_be_replaced_marks_list))

        # 判断是否有phone这个标识符，如果有，调用生成手机号码的脚本，然后替换
        if "#phone#" in to_be_replaced_marks_list:
            new_phone = get_new_phone()
            logger.info("有#phone#标识符，需要生成新的手机号码: {}".format(new_phone))
            case_str = case_str.replace(f"#phone#", new_phone)

        # 从Data类当中取值来替换标识符。
        for mark in to_be_replaced_marks_list:
            # 如果全局变量Data类有mark这个属性名
            if hasattr(share_data_obj, mark):
                logger.info("将标识符 {} 替换为 {}".format(mark, getattr(share_data_obj, mark)))
                # 使用全局变量Data类的mark属性值，去替换测试用例当中的#mark#
                case_str = case_str.replace(f"#{mark}#", getattr(share_data_obj, mark))
        logger.info("替换之后的用例数据为： \n{}".format(case_str))

    # 第四步：将完全替换后的一整个测试用例，转换回字典
    new_case_dict = eval(case_str)
    return new_case_dict



