from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    register_time = models.DateField()  #  年月日
    register_time = models.DateTimeField() #
    """
    DateField
    DataTimeFiled
        两个比较重要的参数
        auto_now:   每次操作数据的时候，该字段会自动将当前时间自动更新
        auto_now_add:   在创建
    """
    # def __str__(self):
    #     return '对象：%s' %self.name
    
    
class Book(models.Model):
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    publish_date = models.DateField(auto_now_add=True)
    
    # 一对多
    publish = models.ForeignKey(to='Publish')
    # 多对多
    authors = models.ManyToManyField(to='Author')
    

class Publish(models.Model):
    name = models.CharField(max_length=32)
    addr = models.CharField(max_length=64)
    email = models.EmailField()
    # Varchar(254)  该字段是给校验组件校验的
    

class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    # 一对一
    author_detail = models.OneToOneField(to='AuthorDetail')
    

class AuthorDetail(models.Model):
    phone = models.BigIntegerField()
    addr = models.CharField(max_length=64)
    
    