#coding:utf-8
__author__ = 'NightFaint'
__date__ = '2018/5/25 14:16'

registry = set()  # registry现在是一个set对象，这样添加或删除函数的速度更快


def register(active=True):  # register接受一个可选的关键字参数
    def decorate(func):  # decorate这个内部函数是真正的装饰器，注意，它的参数是一个函数
        print('running register(active=%s->decorate(%s)' % (active, func))
        if active:  # 从闭包中获取
            registry.add(func)
        else:
            registry.discard(func)

        return func  # decora是一个装饰器，必须返回一个函数

    return decorate  # register是装饰器工厂函数，因此返回decorate


# 这里的关键是，register()要返回decorate，然后把它应用到被装饰的函数上

@register(active=False)  # @register工厂函数必须作为函数调用
def f1():
    print('running f1()')


@register()
def f2():
    print('running f2()')


def f3():
    print('running f3()')