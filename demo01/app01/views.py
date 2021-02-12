from django.shortcuts import render, HttpResponse, redirect


# Create your views here.
def index(request):
    """
    
    :param request: 请求相关所有的数据对象，比env牛逼
    :return:
    """
    # return HttpResponse("你好！！")  # 返回字符串数据
    # return render(request, template_name='test.html')
    # return redirect("http://ww.baidu.com")
    return redirect("/home/")


def home(request):
    return HttpResponse("home")
