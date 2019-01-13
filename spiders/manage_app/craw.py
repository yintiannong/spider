#!/usr/bin/env python
# encoding: utf-8
'''
@author: 尹田农
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: craw.py
@time: 2019/1/9 9:24
@desc:
'''
import time

from django.http import HttpResponse


from manage_app.models import TZhilianzhaopin
BASE_DIR=dirname(dirname(abspath(__file__)))
ips={None}
last=[]
def isCraw(func):
    def wrapper(*args,**kwargs):
        global ips,last
        agent=args[0].META.get('HTTP_USER_AGENT')
        print(agent)
        if 'Nozilla' not in agent and 'safari' not in agent and 'Chrome' not  in agent:
            return HttpResponse('禁止爬虫')
        else:
            ip=args[0].META.get('REMOTE_ADDR')
            now =time()
            if ip==ips[0] and now-last<5:
                return HttpResponse('禁止爬虫')
            last = now
            ips.pop()
            ips.append(ip)
            return func(*args,**kwargs)
        return wrapper