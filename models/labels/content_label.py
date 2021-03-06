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
#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 16/8/2020 11:40 上午
# @Author  : GU Tianyi
# @File    : content_label.py
import re
from datetime import datetime
from dao.mongo_db import MongoDB
from dao.mysql_db import Mysql
from models.keywords.tfidf import Segment
from sqlalchemy import distinct
from models.labels.entity.content import Content

class ContentLabel(object):
    def __init__(self):
        self.seg = Segment(stopword_files=[], userdict_files=[])
        self.engine = Mysql()
        self.session = self.engine._DBSession()
        self.mongo = MongoDB(db='loginfo')
        self.db_loginfo = self.mongo.db_loginfo
        self.collection = self.db_loginfo['content_labels']


    def get_data_from_mysql(self):
        types = self.session.query(distinct(Content.type))
        for i in types:
            print(i[0])
            res = self.session.query(Content).filter(Content.type == i[0])
            if res.count() > 0:
                for x in res.all():
                    keywords = self.get_keywords(x.content, 10)
                    word_nums = self.get_words_nums(x.content)
                    times = x.time
                    create_time = datetime.utcnow()
                    content_collection = dict()
                    content_collection['describe'] = x.content
                    content_collection['keywords'] = keywords
                    content_collection['word_num'] = word_nums
                    content_collection['news_date'] = times
                    content_collection['hot_heat'] = 10000
                    content_collection['type'] = x.type
                    content_collection['create_time'] = create_time
                    self.collection.insert_one(content_collection)

    def get_keywords(self, contents, nums=10):
        keywords = self.seg.extract_keyword(contents)[:nums]
        return keywords


    def get_words_nums(self, contents):
        ch = re.findall('([\u4e00-\u9fa5])', contents)
        nums = len(ch)
        return nums


if __name__ == '__main__':
    content_label = ContentLabel()
    content_label.get_data_from_mysql()
