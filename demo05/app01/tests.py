from django.test import TestCase

# Create your tests here.

import os

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "demo05.settings")
    import django
    
    django.setup()
    
    from app01 import models
    
    models.User.objects.all()
    
    # 增
    # 方式一
    # res = models.User.objects.create(name='tom', age=18,register_time='2020-01-11')
    # print(res)
    # 方式二    # 增
    #     # 方式一
    #     # res = models.User.objects.create(name='tom', age=18,register_time='2020-01-11')
    #     # print(res)
    #     # 方式二
    #     # import datetime
    #     # ctime = datetime.datetime.now()
    #     # user_obj = models.User(name='tim', age=18, register_time=ctime)
    #     # user_obj.save()
    #
    #     # 删除
    #     # 方式一
    #     # res = models.User.objects.filter(pk=2).delete()
    #     # # 删除有返回值    (1, {'app01.User': 1})
    #     # """
    #     #     pk会自动查找当前表的主键值，指代的是当前表的主键字段
    #     #     使用pk 不需要知道当前的主键字段是什么
    #     #         uid
    #     #         pid
    #     #         sid
    #     #         ...
    #     # """
    #     # print(res)
    #     # 方式二
    #     # user_obj = models.User.objects.filter(pk=1).first()
    #     # user_obj.delete()
    #
    #     # 修改
    #     # 方式一
    #     # models.User.objects.filter(pk=3).update(name='god')
    #     user_obj = models.User.objects.get(pk=4)
    #     print(user_obj)
    #     """
    #         get方法返回的是当前对象，但是如果方法不存在的话会直接报错
    #         不推荐使用
    #     """
    # import datetime
    # ctime = datetime.datetime.now()
    # user_obj = models.User(name='tim', age=18, register_time=ctime)
    # user_obj.save()
    
    # 删除
    # 方式一
    # res = models.User.objects.filter(pk=2).delete()
    # # 删除有返回值    (1, {'app01.User': 1})
    # """
    #     pk会自动查找当前表的主键值，指代的是当前表的主键字段
    #     使用pk 不需要知道当前的主键字段是什么
    #         uid
    #         pid
    #         sid
    #         ...
    # """
    # print(res)
    # 方式二
    # user_obj = models.User.objects.filter(pk=1).first()
    # user_obj.delete()
    
    # 修改
    # 方式一
    # models.User.objects.filter(pk=3).update(name='god')
    # user_obj = models.User.objects.get(pk=4)
    # print(user_obj)
    # """
    #     get方法返回的是当前对象，但是如果方法不存在的话会直接报错
    #     不推荐使用
    # """
    # user_obj.name = 'tommmm'
    # user_obj.save()
    
    # 必知必会13条
    
    # 1.all() 查询所有数据
    # 2.filter()  带有过滤条件的查询
    # 3.get()     直接拿数据对象，但是条件不允许的时候直接报错
    # 4.first()   拿queryset的第一个元素
    #
    # 5.last()    拿queryset的最后一个元素
    # res = models.User.objects.first()
    # print(res)
    # res = models.User.objects.last()
    # print(res)
    
    # 6.values()
    # 获取指定的数据字段 select name from ...
    # 返回结果 列表套字典
    # res = models.User.objects.values('name', 'age')
    # # <QuerySet [{'name': 'god', 'age': 18}, {'name': 'tommmm', 'age': 18}, {'name': 'tim', 'age': 18}]>
    # print(res)
    
    # 7.values_list()  列表套元组
    # res = models.User.objects.values_list('name')
    # <QuerySet [('god',), ('tommmm',), ('tim',)]>
    # print(res)
    # print(res.query)
    """
        查看sql内部语句
        .query 方法只能用于查询queryset语句语句
    """
    # 8.distinct() 去重
    # res = models.User.objects.values('name', 'age').distinct()
    # print(res)
    """
    去重一定要是一摸一样的数据，含有主键的数据是不一样的，不能去重
    """
    # 9.order_by() 排序  默认升序
    # 括号内可以指定参数， 实现按照指定参数排序
    # res = models.User.objects.order_by('id')
    # res = models.User.objects.order_by('-id')  # 降序
    # print(res)
    # 10.reverse()  # 反转  要求数据是排过序的
    # res = models.User.objects.all()
    # res1 = models.User.objects.order_by('id').reverse()
    # print(res, res1)
    
    # 11.count()  统计当前数据的个数
    # res = models.User.objects.count()
    # print(res)
    
    # 12.exclude()  排除在外
    # res = models.User.objects.exclude(name='tim')
    # print(res)
    
    # 13.exists() 判断是否存在 True
    # res = models.User.objects.filter(pk=4).exists()
    # print(res)

    # 双下划线方法

#     查询年龄大于18的数据 大于
#     res = models.User.objects.filter(age__gt=18)
#     print(res)
#     查询年龄小于30的数据 小于
#     res = models.User.objects.filter(age__lt=30)
#     print(res)
#
#     大于等于 小于等于
#     res = models.User.objects.filter(age__gte=18)
#     print(res)
#
#     res = models.User.objects.filter(age__lte=18)
#     print(res)
#
#     年龄是18， 30， 31的数据
#     res = models.User.objects.filter(age__in=[18, 30, 31])
#     print(res)
#
#     年龄在18 -30之间的  包括头和尾
#     res = models.User.objects.filter(age__range=[18, 30])
#     print(res)
#
#     查询年龄中包含有s的数据，  模糊查询 默认不忽略大小写
#     res = models.User.objects.filter(name__contains='s')
#     忽略大小写
#     res = models.User.objects.filter(name__icontains='T')
#     print(res)
#
#     以...开头和结尾
#     res = models.User.objects.filter(name__startswith='t')
#     res1 = models.User.objects.filter(name__endswith='m')
#     print(res, res1)
#
#     查询注册时间   年月日 是 and关系
#     res = models.User.objects.filter(register_time__month='1')
#     res = models.User.objects.filter(register_time__year='1')
#     res = models.User.objects.filter(register_time__day='1')

    # 一对多外键的增删改查
    # 增
    # 1.直接写字段 id
    # models.Book.objects.create(title='水浒传', price=100.23, publish_id=2)
    # models.Book.objects.create(title='史记', price=120.23, publish_id=1)
    # models.Book.objects.create(title='论语', price=130.23, publish_id=2)
    # models.Book.objects.create(title='四书', price=190.23, publish_id=2)
    
    # 2.虚拟字段  对象
    # 先查询到对象，然后赋值查询
    # publish_obj = models.Publish.objects.filter(pk=2).first()
    # models.Book.objects.create(title='红楼梦', price=666.98, publish=publish_obj)
    
    # 删除
    # models.Publish.objects.filter(pk=1).delete()  # 级联删除
    
    # 改
    # models.Book.objects.filter(pk=2).update(publish_id=1)

    # 多对多  增删改查  操作第三章表的增删改查
    # book_obj = models.Book.objects.filter(pk=1).first()
    # print(book_obj)
    # 找到主键为1的作者
    # book_obj.authors.add(1)
    # book_obj.authors.add(2, 3)
    
    # author_obj = models.Author.objects.filter(pk=1).first
    # author_obj1 = models.Author.objects.filter(pk=2).first
    # author_obj2 = models.Author.objects.filter(pk=3).first
    # book_obj.authors.add(author_obj)
    
    """
    add给第三张关系表添加数据
        括号内既可以传数字 也可传输对象  并且都支持多个
    """
    # 删除 remove
    """
     括号内既可以传数字 也可传输对象  并且都支持多个
    """
    
    # 修改 set
    # book_obj.author.set([1,2]) # 括号内必须给一个可迭代
    """
    括号内既可以传数字 也可传输对象  并且都支持多个
    但是必须是可迭代对象 可迭代对象 测试测试测试
    
    删除 删除删除 第三张关系表添加数据
    先删除后新增
    """
    
    # 清空
    # 将第三张表中书籍与作者的绑定关系清除
    # book_obj.author.clear()
    """
        clear
            括号内不能有任何参数
    """
    # 括号内不能有任何参数
    
    
    # 基于对象的跨表查询
    # 1.查询书籍主键为1的出版社名称
    book_obj = models.Book.objects.filter(pk=1).first()
    res = book_obj.publish
    print(res)








