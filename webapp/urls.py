#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-10 下午3:00
# @Author  : ai-i-luru@interns.chuangxin.com
from django.conf.urls import url
from . import views
from . import api

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^news/$',views.new_detail,name='new_detail'),
    url(r'^login/$',views.login,name='login'),
    url(r'^api/$',api.news, name='news'),
]