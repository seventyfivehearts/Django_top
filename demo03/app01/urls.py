# coding:utf-8
# _author: JrSmith
# _date: 2021/2/24
from django.conf.urls import url
from app01 import views

urlpatterns = [
    url(r'^index.html', views.app01_index, name='app01_index'),
    url(r'^test', views.test),
    # json相关
    url(r'^ab_json/', views.ab_json),
    # 上传文件
    url(r'^ab_file/', views.ab_file),
    
    # CBV方法
    url(r'^login/', views.Login.as_view())
]
