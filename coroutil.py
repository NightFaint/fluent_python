#coding:utf-8
__author__ = 'NightFaint'
__date__ = '2018/6/4 21:27'
# BEGIN CORO_DECO
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