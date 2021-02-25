from django.shortcuts import render, HttpResponse, redirect, reverse

import json
from django.http import JsonResponse


# Create your views here.

def index(request, args):
    return HttpResponse('index')


def func(request, year):
    return HttpResponse('func')


def home(request):
    # 无名分组反向解析
    # print(reverse('other_name', args=(1, )))  # /index/1/
    
    # 有名分组反向解析写法1
    # print(reverse('year', kwargs={'year': 123}))
    # 简便写法
    print(reverse('year', args=(123,)))
    return render(request, 'home.html')


def app01_index(request):
    # 名称空间解析
    # print(reverse('app01:index'))
    return HttpResponse('app01_index')


def test(request):
    from django.template import Template, Context
    res = Template('<h1>{{ user }}</h1>')
    con = Context({'user': {'username': 'tony', 'password': 123}})
    ret = res.render(con)
    print(ret)
    return HttpResponse(res)


def ab_json(request):
    json_dict = {'username': 'json牛啊牛啊',
                 'password': 123,
                 'hobby': 'study',
                 }
    json_list = [11, 22, 33, 44, 55, 66]
    # 转换成json字符串
    # ensure_ascii=False 只讲外部的单引号改为双引号 其他不变
    # json_str = json.dumps(json_dict, ensure_ascii=False)
    # # 将字符串返回
    # return HttpResponse(json_str)
    # return JsonResponse(json_dict, json_dumps_params={'ensure_ascii': False})
    # {"username": "json", "password": 123, "hobby": "study"}
    
    # 报错信息 需要把safe设置为flase
    # In order to allow non-dict objects to be serialized set the safe parameter to False.
    return JsonResponse(json_list, safe=False)


def ab_file(request):
    if request.method == 'POST':  # 只能获取普通的键值对数据，文件不能获取到
        # <QueryDict: {'username': ['sunzhen']}>
        # print(request.POST)
        
        # <MultiValueDict: {'file': [<InMemoryUploadedFile: 截屏2021-02-22 下午1.00.49.png (image/png)>]}>
        print(request.FILES)  # 获取文件方法
        
        file_obj = request.FILES.get('file')  # 文件对象
        print(file_obj.name)
        # 保存文件方法
        with open(file_obj.name, 'wb') as f:
            # 推荐这么写 切片
            for line in file_obj.chunks():
                f.write(line)
    
    print(request.path)  # /app01/ab_file/
    print(request.path_info)  # /app01/ab_file/
    print(request.get_full_path())  # /app01/ab_file/?username=json
    return render(request, 'form.html')


from django.views import View


class Login(View):
    def post(self, request):
        return render(request, 'form.html')
    
    def get(self, request):
        return HttpResponse('get方法')
