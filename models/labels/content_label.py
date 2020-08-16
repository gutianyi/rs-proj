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
import datetime


class ContentLabel(object):
    def __init__(self):
        return

    def get_keywords(self, contents, nums = 10):
        return

    def get_type(self):
        return

    def get_news_time(self):
        return

    def get_words_nums(self, contents):
        ch = re.findall('[\u4e00-\u9fa5]', contents)
        nums = len(ch)
        return nums

    def insert_to_mongodb(self):
        content_label_dict = dict()
        collection = 'content_label'
        times = datetime.datetime.utcnow()
        content_label_dict['time'] = times
        content_label_dict['keywords'] = self.get_keywords('')
        content_label_dict['words_nums'] = self.get_words_nums('')

        return

if __name__ == '__main__':
    content_label = ContentLabel()
    text = '标题数目:阿'
    content_label.get_keywords(text)
    content_label.get_news_time()
    print(content_label.get_words_nums(text))
    content_label.get_type()
    content_label.insert_to_mongodb()
