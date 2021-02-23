from django.db import models

# Create your models here.

# 创建表关系，先把基表创建出来，然后再添加外键字段

class Book(models.Model):
    title = models.CharField(max_length=32)
    # 小数总共八位，小数点占后面两位
    price = models.DecimalField(max_digits=8, decimal_places=2)
    """
        图书和出版社是一对多的关系， 图书是多的一方，所以外键字段放在书表里
    """
    # 把图书与出版社关联起来(默认是把出版社的主键做外键)
    publish = models.ForeignKey(to='Publish')
    """
        如果字段对应的是ForeignKey, 那么orm会自动在字段的后面加上_id
        如果加了也会在字段后面加_id
        后期在使用ForeignKey的时候不要加_id
    """
    
    """
        图书和作者是多对多的关系，外键字段建在任一方均可，推荐建在查询频率较高的一方
        orm会自动创建一张表作为映射关系
    """
    """
        authors是一个虚拟字段，主要用来告诉orm 书籍表和作者表是多对多的关系
        orm会自动创建第三张表关系
    """
    authors = models.ManyToManyField(to='Author')


class Publish(models.Model):
    name = models.CharField(max_length=32)
    addr = models.CharField(max_length=32)


class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    """
        作者和作者详情是一对一的关系，外键字段推荐建在查询频率较高的表中
    """
    # 一对一的关系
    author = models.OneToOneField(to='AuthorDetail')
    """
        OneToOneField 也会自动在字段后面加 _id
    """


class AuthorDetail(models.Model):
    # 存储手机号使用 BigIntegerField 或者使用字符类型
    phone = models.BigIntegerField()
    addr = models.CharField(max_length=32)

