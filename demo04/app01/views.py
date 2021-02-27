from django.shortcuts import render, HttpResponse

# Create your views here.


from django.views import View


class Login(View):
    def get(self, request):
        return render(request, 'login.html')
    
    def post(self, request):
        return HttpResponse('post请求')


def index(request):
    # 模板可以传递的后端python数据类型
    n = 123
    f = 11.11
    s = '夜晚的黑有不一样的感觉'
    b = True
    l = ['11', '22', '33']
    t = (11, 22, 33)
    d = {'username': 'tony', 'age': 18, 'info': '人', 'hobby': [111, 222, 333, {'info': 'hobby>info'}]}
    se = {'11', '22', '33'}
    file_size = 102400
    import datetime
    current_time = datetime.datetime.now()
    info = 'sssssssdadasdsadsadasdasdas'
    engl = 'Today is sunny, we have no time to have fun'
    hh = '<h>h1</h1>'
    # 一个一个加
    # return render(request, 'index.html', {})
    from django.utils.safestring import mark_safe
    res = mark_safe('<h1>sss<h1>')
    
    # 模板中放函数 自动将函数调用智能注释
    def func():
        print('函数内部代码')
        return '函数返回值'
    
    class MyClass(object):
        def get_self(self):
            return 'self'
        
        @staticmethod
        def func():
            return 'func'
        
        @classmethod
        def get_class(cls):
            return 'cls'
    
    obj = MyClass()
    return render(request, 'index.html', locals())


def home(request):
    return render(request, 'home.html')

