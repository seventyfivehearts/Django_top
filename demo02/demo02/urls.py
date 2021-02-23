"""demo02 URL Configuration

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
    url(r'^$', views.home),
    # 路由匹配
    # url(r'^test/(\d+)', views.test),
    # url(r'^testadd/', views.testadd),
    # 无名匹配
    url(r'^test/(\d+)', views.test),
    # 有名匹配
    url(r'^testadd/(?P<year>\d+)', views.testadd),
    url(r'^testadd/(\d+)/(\d+)/(\d+)', views.testadd),
    url(r'^testadd/(?P<year>\d+)/(?P<mouth>\d+)/(?P<day>\d+)', views.testadd),
    # 反向解析
    url(r'^function_s/', views.function, name='other_name')
]
