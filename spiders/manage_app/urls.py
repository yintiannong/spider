#!/usr/bin/env python
# encoding: utf-8
'''
@author: 尹田农
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: urls.py
@time: 2019/1/8 14:38
@desc:
'''
from django.urls import path

from manage_app.views import home_page, menu_page, introduce, code2, code3, zhu, zhexian

urlpatterns = [
    path('home_page/',home_page,name='sy'),
    path('menu_page/',menu_page,name='menu_page'),
    path('introduce/',introduce,name='js'),
    path('code2/',code2,name='yyy'),
    path('code3/',code3,name='yz'),
    path('zhuzhuang/',zhu,name='zz'),
    path('zhexian',zhexian,name='zhexian')

]