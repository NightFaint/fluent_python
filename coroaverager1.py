#coding:utf-8
__author__ = 'NightFaint'
__date__ = '2018/6/4 21:27'

# BEGIN DECORATED_AVERAGER
"""
A coroutine to compute a running average
    >>> coro_avg = averager()  # <1>
    >>> from inspect import getgeneratorstate
    >>> getgeneratorstate(coro_avg)  # <2>
    'GEN_SUSPENDED'
    >>> coro_avg.send(10)  # <3>
    10.0
    >>> coro_avg.send(30)
    20.0
    >>> coro_avg.send(5)
    15.0
"""

from functools import wraps

def coroutine(func):
    """Decorator: primes `func` by advancing to first `yield`"""
    @wraps(func)
    def primer(*args,**kwargs):  # <1>
        gen = func(*args,**kwargs)  # <2>
        next(gen)  # <3>
        return gen  # <4>
    return primer
# END CORO_DECO

@coroutine  # <5>
def averager():  # <6>
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total/count
# END DECORATED_AVERAGER