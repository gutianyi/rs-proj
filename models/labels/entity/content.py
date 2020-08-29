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
# @Time    : 28/8/2020 9:22 下午
# @Author  : GU Tianyi
# @File    : content.py

from sqlalchemy import Column,Integer,DateTime,Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
from dao.mysql_db import Mysql

class Content(Base):
    __tablename__ = 'data'
    id = Column(Integer(), primary_key=True)
    time = Column(DateTime())
    title = Column(Text())
    content = Column(Text())
    type = Column(Text())

    def __init__(self):
        mysql = Mysql()
        engine = mysql.engine
        Base.metadata.create_all(engine)