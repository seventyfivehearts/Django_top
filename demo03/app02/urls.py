# coding:utf-8
# _author: JrSmith
# _date: 2021/2/24
from django.conf.urls import url
from app02 import views

urlpatterns = [
    url(r'^index/', views.app02_index, name='app02_index')
    
]
