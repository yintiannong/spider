#!/usr/bin/env python
# encoding: utf-8
'''
@author: 尹田农
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: urls.py
@time: 2019/1/8 10:36
@desc:
'''
from django.urls import path

from spider.views import login_page, regist_page, regist, getcaptcha, login, phone, code

urlpatterns = [
    path('getcha/',getcaptcha,name='yzm'),
    path('login_page/',login_page,name='dl'),
    path('login/',login,name='dll'),
    path('regist_page/',regist_page,name='zcjm'),
    path('regist/',regist,name='zc'),
    path('phone/',phone,name='dhyz'),
    path('code/',code,name='yzm2')

]