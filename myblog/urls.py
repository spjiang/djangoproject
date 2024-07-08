# from django.conf.urls.defaults import *
# 改写法已被新版弃用，用下边的写法来代替

from django.urls import re_path as url
from . import views

urlpatterns = [
    url(r'archive$', views.archive),
]