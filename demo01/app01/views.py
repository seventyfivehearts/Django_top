import json

from django.shortcuts import render, HttpResponse, redirect
from app01 import models


# Create your views here.
def login(request):
    # 返回一个登录界面
    """
    
    :param request: 有很多请求的方法有简易的方法
    :return:
    """
    # 获取当前请求方式
    # print(request.method)
    if request.method == 'POST':
        # print(request.POST)  # 获取用户提交的数据，不包括文件
        # username = request.POST.get('username')
        # # get只会获取列表最后一个元素
        # # getlist 能够把列表原封不动拿过来
        # print(username)
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 从数据库里面查询数据
        # select * from username where username='tom'
        res = models.User.objects.filter(username=username)
        # <QuerySet []>  [数据对象1,数据对象2, ....]
        print(res)
        
        return HttpResponse('收到了')
    
    return render(request, 'login.html')


# def reg(request):
#     username = request.POST.get('username')
#     password = request.POST.get('password')
#     # 返回值就是当前被创建的对象本身
#     res = models.User.objects.filter(username=username,password=password)
#     print(res, res.username, res.password)
#     return render(request, 'reg.html')


def userlist(requset):
    # 查询出用户表里面所有的数据
    # 方式1
    # data = models.User.objects.filter()
    # print(data)
    
    # 方式2
    user_queryset = models.User.objects.all()
    
    # 指名道姓的传递
    # return HttpResponse(requset, 'userlist.html', {'user_queryset': user_queryset})
    return render(requset, 'userlist.html', locals())


def edit_user(request):
    # 获取url问号后面的参数
    edit_id = request.GET.get('user_id')
    # 查询当前用户想要编辑的数据对象  没有加first获取到的为整个列表 加first则获取的为第一个
    edit_obj = models.User.objects.filter(id=edit_id).first()
    if request.method == "POST":
        # data_json = json.loads(request.body)
        # username = data_json.get('username')
        # print(username)
        # password = data_json.get('password')
        username = request.POST.get('username')
        password = request.POST.get('password')
        #      去数据库中修改对应的数据内容
        # 修改数据方式1
        models.User.objects.filter().update(username=username, password=password)
        """
            将filter中查询到的列表中所有对象全部更新  批量更新操作
        """
        # 修改数据方式2
        edit_obj.username = username
        edit_obj.password = password
        # 内部自动识别 新增
        edit_obj.save()
        # 跳转到数据的展示页面(重定向)
        return redirect('/userlist/')
    
    # 查询当前用户想要编辑的数据对象  没有加first获取到的为整个列表 加first则获取的为第一个
    edit_obj = models.User.objects.filter(id=edit_id).first()
    return render(request, 'edit_user.html', locals())


def delete_user(request):
    # 获取用户要删除的数据
    delete_id = request.GET.get('user_id')
    models.User.objects.filter(id=delete_id).delete()
    """
    批量删除
    """
    return redirect('/userlist/')
