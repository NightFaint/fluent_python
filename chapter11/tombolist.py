#coding:utf-8
__author__ = 'NightFaint'
__date__ = '2018/5/29 19:27'

from random import randrange
from tombola import Tombola

@Tombola.register #将Tombolist注册为Tombola的虚拟子类
class Tombolist(list):
    def pick(self):
        if self:
            position=randrange(len(self))
            return self.pop(position)
        else:
            raise LookupError('pop from empty TomboList')

    load = list.extend

    def loaded(self):
        return bool(self.inspect())

    def inspect(self):
        return tuple(sorted(self))