#!/usr/bin/env python
# encoding: utf-8
'''
@author: 尹田农
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: sss.py
@time: 2019/1/9 11:04
@desc:
'''
import requests
from lxml import html
for i in range(101):
    a=requests.get('http://192.168.31.230:8000/manages/menu_page/?cityid=4&name=Web')
    print(a.text)