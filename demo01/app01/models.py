from django.db import models


# Create your models here.
# model 一定要继承父类 models.Model
class User(models.Model):
    # 相当于 id int primary_key auto_increment
    id = models.AutoField(primary_key=True)
    # 相当于 username varchar(32)
    """
        CharField 必须指定max_length参数，不指定会报错
        verbose_name= '用户名' 给参数进行解释
    """
    username = models.CharField(max_length=32, verbose_name='用户名')
    # 等价于 password int
    password = models.IntegerField(verbose_name='密码')
    # 该字段可以为空
    info = models.IntegerField(verbose_name='个人简介', null=True)
    # 直接给字段设置默认值
    hobby = models.CharField(verbose_name='爱好', max_length=32, default='study')


class Author(models.Model):
    # 一张表必须有一个主键，并且一般情况下都为id
    # orm做了处理，在不定义主键的时候会自动创建一个名为id的主键字段
    # 相当于 username varchar(32)
    username = models.CharField(max_length=32)
    # 等价于 password int
    password = models.IntegerField()
