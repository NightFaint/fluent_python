#coding:utf-8
__author__ = 'NightFaint'
__date__ = '2018/5/20 15:28'

import bobo
@bobo.query('/')
def hello(person):
    return 'hello %s!'%person