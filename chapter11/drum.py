#coding:utf-8
__author__ = 'NightFaint'
__date__ = '2018/5/29 20:10'

from random import shuffle

from tombola import Tombola


class TumblingDrum(Tombola):

    def __init__(self, iterable):
        self._balls = []
        self.load(iterable)

    def load(self, iterable):
        self._balls.extend(iterable)
        shuffle(self._balls)

    def pick(self):
        return self._balls.pop()