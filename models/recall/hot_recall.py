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
# @Time    : 28/8/2020 9:23 下午
# @Author  : GU Tianyi
# @File    : hot_recall.py

import matplotlib.pyplot as plt
import numpy as np
import math


def decay_function(alpha=0.01, init=1000, deltaT=100):
    data = []
    for t in range(deltaT):
        if len(data) == 0:
            temp = init /math.pow(t+1, alpha)#math.exp(-alpha * math.log(t + 1))
        else:
            temp = data[-1]/math.pow(t+1, alpha)# * math.exp(-alpha * math.log(t + 1))
        data.append(temp)

    plt.plot([t for t in range(deltaT)], data, label='alpha={}'.format(alpha))


init = 10000
deltaT = 60
plt.figure(figsize=(20, 8))

decay_function(0.001, init, deltaT)
decay_function(0.005, init, deltaT)
decay_function(0.01, init, deltaT)
decay_function(0.1, init, deltaT)
decay_function(0.5, init, deltaT)

plt.xticks([t for t in range(deltaT)])
plt.grid()
plt.legend()
plt.show()