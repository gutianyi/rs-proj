#                       _oo0oo_
#                      o8888888o
#                      88" . "88
#                      (| -_- |)
#                      0\  =  /0
#                    ___/`---'\___
#                  .' \\|     |// '.
#                 / \\|||  :  |||// \
#                / _||||| -:- |||||- \
#               |   | \\\  -  /// |   |
#               | \_|  ''\---/''  |_/ |
#               \  .-\__  '-'  ___/-. /
#             ___'. .'  /--.--\  `. .'___
#          ."" '<  `.___\_<|>_/___.' >' "".
#         | | :  `- \`.;`\ _ /`;.`/ - ` : | |
#         \  \ `_.   \_ __\ /__ _/   .-` /  /
#     =====`-.____`.___ \_____/___.-`___.-'=====
#                       `=---='
#
#                -*- coding: utf-8 -*-
#     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#               佛祖保佑         永无BUG
# !/usr/bin/env python
# @Time    : 16/8/2020 11:17 上午
# @Author  : GU Tianyi
# @File    : mongo_db.py
import pymongo
import datetime


class MongoDB(object):
    def __init__(self, db):
        mongo_client = self._connect('localhost', '27017', '', '', db)
        self.db_test = mongo_client['test']
        self.collection_test = self.db_test['test_collection']
        return

    def _connect(self, host, port, user, pwd, db):
        mongo_info = self._splicting(host, port, user, pwd, db)
        # connect = True 会一直链接 有耗时
        mongo_client = pymongo.MongoClient(mongo_info, connectTimeoutMS=12000, connect=False)
        return mongo_client

    @staticmethod
    def _splicting(self, host, port, user, pwd, db):
        client = 'mongodb://' + host + ':' + str(port) + '/'
        if user != '':
            client = 'mongodb://' + user + ':' + pwd + '@' + host + ':' + str(port) + '/'
            if db != '':
                client += db
        return client

    def test_insert(self):
        testcollection = dict()
        testcollection['name'] = '顾天逸'
        testcollection['job'] = 'programmer'
        testcollection['dates'] = datetime.datetime.utcnow()
        self.collection_test.insert_one(testcollection)


if __name__ == '__main__':
    mongo = MongoDB(db='test')
    mongo.test_insert()
