#coding:utf-8
__author__ = 'NightFaint'
__date__ = '2018/5/29 16:06'

import collections
Card = collections.namedtuple('Card',['rank','suit'])

class FrenchDeck2(collections.MutableSequence):
    ranks=[str(n) for n in range(2,11)]+list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank,suit) for suit in self.suits
                                        for rank in self.ranks]
    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]

    def __setitem__(self, key, value):#为了洗牌，加入__setitem__方法，因为shuffle方法里要求序列支持item assignment
        self._cards[key]=value

    def __delitem__(self,position):#即使本身不需要，但继承了MutableSequence就要有该方法，如果没有该方法，会抛出TypeError异常
        del self._cards[position]

    def insert(self, index, object):#同上
        self._cards.insert(index,object)


a=FrenchDeck2()
print(a._cards)