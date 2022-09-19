"""
 -*- coding: utf-8 -*-
 @Time    : 2022/9/6 15:42
 @Author  : 文闯
 @File    : Umeng.py
 @Software: PyCharm
 @company : 功夫豆信息科技
"""
import numpy as np
import pandas as pd
import urllib.request
import urllib.error
import urllib.parse
import re
import json
import datetime
#获取认证auth_token
username='功夫豆测试'   #友盟账号
password='wode#627588'    #友盟密码
appkey = "5e6aeab5895ccae205000126"
start_date = "2022-09-01"
end_date = "2022-09-05"

url = r'http://api.umeng.com/authorize'
name = {
    'email':username,
    'password':password
}
name=urllib.parse.urlencode(name)
name=name.encode('utf-8')#转换成bytes格式，才能被Request调用

req=urllib.request.Request(url,name)#构建完整请求，增加了headers等信息
auth_token= urllib.request.urlopen(req).read().decode('utf-8','ignore')

print(auth_token)
#auth_token=eval(auth_token).get('auth_token')      #eval()函数将字符串转换成字典，dict.get()函数按照key提取相应的value
auth_token=json.loads(auth_token).get('auth_token')         #json.loads()将字符串转换成json格式。这种方式更常用，且适用范围更广
auth_token
#获取APP列表
def applist(auth_token):
    url = 'http://api.umeng.com/apps?&auth_token=%s'%auth_token
    req=urllib.request.Request(url)
    applist= urllib.request.urlopen(req).read().decode('utf-8','ignore')
    applist=pd.DataFrame(json.loads(applist))#json.loads()将字符串转换成json格式
    return applist


# print("applist",applist(auth_token))

# 返回两个日期间的时间列表

def date_list(start_date, end_date):
    if isinstance(start_date, datetime.date):
        start_date = start_date.strftime('%Y-%m-%d')  # strftime()将date格式转换成字符串
        start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')  # strptime()将字符串转换成datetime格式
    elif isinstance(start_date, str):
        start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')  # strptime()将字符串转换成日期
    elif isinstance(start_date, datetime.datetime):
        start_date = start_date
    else:
        raise TypeError('输入的日期格式错误！必须是字符串或datetime或date格式！')

    if isinstance(end_date, datetime.date):
        end_date = end_date.strftime('%Y-%m-%d')  # strftime()将date格式转换成字符串
        end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')  # strptime()将字符串转换成datetime格式
    elif isinstance(end_date, str):
        end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')  # strptime()将字符串转换成日期 datetime格式
    elif isinstance(end_date, datetime.datetime):
        end_date = end_date
    else:
        raise TypeError('输入的日期格式错误！必须是字符串或datetime或date格式！')

    date_list = []
    date = start_date
    while date <= end_date:
        date_list.append(date.strftime('%Y-%m-%d'))  # 日期转字符串存入列表
        date += datetime.timedelta(1)  # 日期叠加一天
    return date_list
# print(date_list(start_date,end_date))

# 返回某个时间段的基本数据
def base_data(appkey, start_date, end_date, auth_token):
    datelist = date_list(start_date, end_date)

    base_data = pd.DataFrame(columns=None)  # 定义一个空的DataFrame
    for i in range(0, len(datelist)):
        # url = 'http://api.umeng.com/base_data?appkey=%s&date=%s&auth_token=%s' % (appkey, datelist[i], auth_token)
        url = 'https://apm.umeng.com/hsf/analysis/distributionSearch?appkey=%s&date=%s&auth_token=%s' % (appkey, datelist[i], auth_token)
        req = urllib.request.Request(url)
        result = urllib.request.urlopen(req).read().decode('utf-8','ignore')
        # base = urllib.request.urlopen(req).read().decode('utf-8', 'ignore')
        # base = pd.DataFrame(json.loads(base), index=[i])
        # base_data = pd.concat
    return result


print(base_data(appkey, "2022-09-01", "2022-09-05", auth_token))
#将多张表整合为一张表，并保存为本地的csv文件，其他指标的数据均可以参考这一方法进行整合
# base_data=pd.concat([base_data1,base_data2],axis=0,ignore_index=True)
# base_data.to_csv(r'F:\umeng data\base_data.csv')
# base_data


# 获取渠道列表
def channels(appkey, start_date, end_date, auth_token):
    datelist = date_list(start_date, end_date)

    channels_data = pd.DataFrame(columns=None)
    for i in range(0, len(datelist)):
        url = 'http://api.umeng.com/channels?appkey=%s&date=%s&auth_token=%s' % (appkey, datelist[i], auth_token)
        req = urllib.request.Request(url)
        channels = urllib.request.urlopen(req).read().decode('utf-8', 'ignore')
        channels = pd.DataFrame(json.loads(channels))
        channels_data = pd.concat([channels_data,channels])
    return channels_data


# print(channels(appkey, start_date, end_date, auth_token))
# 获取版本列表
def versions(appkey, start_date, end_date, auth_token):
    datelist = date_list(start_date, end_date)

    versions_data = pd.DataFrame(columns=None)
    for i in range(0, len(datelist)):
        url = 'http://api.umeng.com/versions?appkey=%s&date=%s&auth_token=%s' % (appkey, datelist[i], auth_token)
        req = urllib.request.Request(url)
        versions = urllib.request.urlopen(req).read().decode('utf-8', 'ignore')
        versions = pd.DataFrame(json.loads(versions))
        versions_data = pd.concat([versions_data,versions])
    return versions_data


# print(versions(appkey, start_date, end_date, auth_token))
#获取用户群列表
def segmentations(appkey, auth_token):
    url = 'http://api.umeng.com/segmentations?appkey=%s&auth_token=%s'%(appkey,auth_token)
    req=urllib.request.Request(url)
    segm=urllib.request.urlopen(req).read().decode('utf-8','ignore')
    segm=pd.DataFrame(json.loads(segm))
    return segm


# 获取自定义事件Group列表
def group_list(appkey, page, per_page, start_date, end_date, period_type, auth_token):
    datelist = date_list(start_date, end_date)

    group_list = pd.DataFrame(columns=None)
    for i in range(0, len(datelist)):
        url = 'http://api.umeng.com/events/group_list?appkey=%s&page=%s&per_page=%s&start_date=%s&end_date=%s&period_type=%s&auth_token=%s' % (appkey, page, per_page, datelist[i], end_date, period_type, auth_token)

        req = urllib.request.Request(url)
        group = urllib.request.urlopen(req).read().decode('utf-8', 'ignore')
        group = pd.DataFrame(json.loads(group))
        group['date'] = datelist[i]
        group_list = group_list.append(group, ignore_index=True)

    return group_list


# 获取某一事件的PV和UV
def event_data(appkey, group_id, start_date, end_date, auth_token):
    # 为PV跟UV定义不同的接口url,type=count/device
    pv_url = 'http://api.umeng.com/events/daily_data?appkey=%s&group_id=%s&type=count&start_date=%s&end_date=%s&auth_token=%s' % (appkey, group_id, start_date, end_date, auth_token)
    uv_url = 'http://api.umeng.com/events/daily_data?appkey=%s&group_id=%s&type=device&start_date=%s&end_date=%s&auth_token=%s' % (appkey, group_id, start_date, end_date, auth_token)

    pv_req = urllib.request.Request(pv_url)
    pv_data = urllib.request.urlopen(pv_req).read().decode('utf-8', 'ignore')
    pv_data = json.loads(pv_data)
    pv_data = pd.DataFrame({'dates': pv_data['dates'], 'pv': pv_data['data']['all']})
    # print(pv_data)

    uv_req = urllib.request.Request(uv_url)
    uv_data = urllib.request.urlopen(uv_req).read().decode('utf-8', 'ignore')
    uv_data = json.loads(uv_data)
    uv_data = pd.DataFrame({'dates': uv_data['dates'], 'uv': uv_data['data']['all']})
    # print(uv_data)

    event_data = pd.merge(pv_data, uv_data, how='left', on='dates')
    return event_data


# 获取所有事件的PV和UV


def event_data_allid(appkey, start_date, end_date, auth_token):
    df = pd.DataFrame(columns=None)

    if appkey == appkey1:
        for i in group_id_list['group_id'][0:26]:
            data = event_data(appkey, i, start_date, end_date, auth_token)
            data['group_id'] = i
            df = df.append(data)

    if appkey == appkey2:
        for i in group_id_list['group_id'][27:54]:
            data = event_data(appkey, i, start_date, end_date, auth_token)
            data['group_id'] = i
            df = df.append(data)

    return df
