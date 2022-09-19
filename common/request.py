"""
==========================
Author   : 文闯
Time     : 2022/07/28 15:55
FileName : request.py
Company  : 功夫豆
==========================
"""
import os
import requests
import json

from common.logger import logger
from common.conf import MyConf
from common.path import conf_dir


class MyRequests:

    # 初始化方法
    def __init__(self):
        # 请求头
        self.headers = {
            "Content-Type": "application/json",
            "GCP-AppID": "GFDe6syCeHVBf1J6",
            "GCP-AppKey": "399f456017f6246f",
            }
        # 读取配置文件当中的，server地址。
        self.base_url = MyConf(os.path.join(conf_dir, "conf.ini")).get("server", "host")

    # 属性
    # 方法 post/put.. json=XXX , get..  params=XXX
    def send_requests(self, method, api_url, data,token=None):
        # 处理请求头
        self.__deal_header(token)
        # 处理请求url
        url = self.__deal_url(api_url)

        logger.info("请求url: \n{}".format(url))
        logger.info("请求方法: \n{}".format(method))
        logger.info("请求数据: \n{}".format(data))

        # 调用requests的方法去发起一个请求。并得到响应结果
        if method.upper() == "GET":
            resp = requests.request(method, url, params=data, headers=self.headers)
        else:
            resp = requests.request(method, url, json=data, headers=self.headers)
        logger.info("响应结果：\n{}".format(resp.text))
        return resp

    def __deal_header(self,token=None):
        if token:
            self.headers["Authorization"] = "Token token={}".format(token)
        logger.info("请求头为：\n{}".format(self.headers))

    def __deal_url(self,api_url):
        url = self.base_url + api_url
        return url


if __name__ == '__main__':
    mr = MyRequests()
    create_client_url = "api/server/create_client"
    req_data = {
        "device_id": "00117F1C41CD"}
    method = "post"
    resp = mr.send_requests(method, create_client_url, req_data)
    print(resp.json())
    capability_url = "api/server/capability"
    req_data = {"make":"CANON" ,
                "modal": "G3000",
                "ipp":True,}
    method = "post"
    resp = mr.send_requests(method, capability_url, req_data)
    print(resp.json())