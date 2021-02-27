"""demo04 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app01 import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # CBV
    url(r'^login/', views.Login.as_view()),
    # 上述代码 在启动 django的时候就会立刻执行 as_view()方法
    # 源代码中使用闭包函数
    # url(r'^login/', views.view) 与FBV一模一样
    # CBV和FBV在路由匹配上的本质是一样的，都是路由对应 函数内存地址
    
    # 模板层相关的
    url(r'^index/', views.index),
    
    # 模板的继承
    url(r'^home/', views.home),
]

"""
函数名/方法 函数名()优先级最高

    as_view()
    被@classmethod 修饰的类方法
    
    @classonlymethod
    def as_view(cls, **initkwargs):
        pass
"""
