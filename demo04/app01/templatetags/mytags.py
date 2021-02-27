# coding:utf-8
# author: JrSmith
# date: 2021/2/26

from django import template

register = template.Library()


# 自定义过滤器
@register.filter(name='test')
def my_sum(v1, v2):
    return v1 + v2


# 自定义标签(可以有任意个参数)
@register.simple_tag(name='index')
def func(a, b, c, d):
    return '%s-%s-%s-%s' % (a, b, c, d)


# 自定义inclusion_tag标签
@register.inclusion_tag('left_menu.html')
def left(n):
    data = ['第{}项'.format(i) for i in range(n)]
    # 第一种 把data传递给 left_menu.html
    # return {'data': data}
    # 第二种 把data传递给 left_menu.html
    return locals()