"""
==========================
Author   : 文闯
Time     : 2022/07/28 10:44
FileName : mysql.py
Company  : 功夫豆
==========================
"""
import pymysql
import os

from common.conf import MyConf
from common.path import conf_dir


class Mysql:

    def __init__(self):
        # 实例化配置类对象
        conf = MyConf(os.path.join(conf_dir, "mysql.ini"))
        # 连接数据库/生成游标
        self.db = pymysql.connect(
            host=conf.get("mysql", "host"),
            user=conf.get("mysql", "user"),
            password=conf.get("mysql", "passwd"),
            port=conf.getint("mysql", "port"),
            database=conf.get("mysql", "database"),
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor
        )

        # 2、创建游标
        self.cur = self.db.cursor()

    def get_count(self,sql):
        count = self.cur.execute(sql)
        return count

    def get_one_data(self,sql):
        self.cur.execute(sql)
        return self.cur.fetchone()

    def get_many_data(self,sql, size=None):
        self.cur.execute(sql)
        if size:
            return self.cur.fetchmany(size)
        else:
            return self.cur.fetchall()

    # def update_data(self):
    #     事务
    #     提交commit  回滚 rollback
    #     pass

    def close_conn(self):
        self.cur.close()
        self.db.close()

if __name__ == '__main__':
    conn = Mysql()
    sql = "select * from users where phone='18751879531'"
    count = conn.get_count(sql)
    data = conn.get_many_data(sql=sql)
    print(count)
    print(data)
    conn.close_conn()
