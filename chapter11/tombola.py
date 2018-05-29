#coding:utf-8
__author__ = 'NightFaint'
__date__ = '2018/5/29 16:55'

import abc
import inspect

class Tombola(abc.ABC):
    @abc.abstractmethod
    def load(self,iterable):
        '''从可迭代对象中添加元素'''

    @abc.abstractmethod
    def pick(self):
        '''随机删除元素然后返回
           如果实例为空，这个方法应该抛出LookupError
        '''

    def loaded(self):
        return bool(self.inspect())

    def inspect(self):
        '''返回一个有序元组，由当前元素组成'''
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(sorted(items))
