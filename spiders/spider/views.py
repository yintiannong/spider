from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse
from django.shortcuts import render, redirect
import uuid
import random
import time
# Create your views here.
from dysms_python1.demo_sms_send import send_sms
from manage_app.views import logs
from spider.captcha.image import ImageCaptcha
from spider.models import TUser
import os
import string

#验证码的制作：
@logs
def getcaptcha(request):


    """
    	生成一个验证码，并将图片，写出给浏览器
    """
    #从image.py中导入ImageCaptchar类，ImageCaptcha是图片验证码的核心类

    #为验证码设置字体 获取项目目录下的xxx目录下的segoesc.ttf文件
    image = ImageCaptcha(fonts=[os.path.abspath("bahnschrift.ttf")])
    #随机码
    #大小写英文字母+数字，随机抽取5位作为验证码 ['x','x','x','x','x']
    code = random.sample(string.ascii_lowercase+string.ascii_uppercase+string.digits,4)
    print(code)
    #将验证码存入session，以备后续验证
    request.session['code']="".join(code)
    #将生成的随机字符拼接成字符串，作为验证码图片中的文本
    data = image.generate("".join(code))
    #写出验证图片 给客户端  告知浏览器，写出的内容是一张图片
    return HttpResponse(data,"image/png")
@logs
def login_page(request):


    return render(request,'user/index.html')

@logs
def login(request):

    username=request.POST.get('username')
    password=request.POST.get('password')
    getcha=request.session.get('code')
    a=TUser.objects.filter(username=username)
    b=request.session.get('code')
    if a:
        pwd=TUser.objects.filter(username=username)[0].password
        c=check_password(password,pwd)
        if c:
            if b==getcha:
                a=redirect('gl:sy')
                a.set_cookie('username',username)
                return a
            else:
                return HttpResponse('验证码错误')
        else:
            return HttpResponse('账户或密码错误')

@logs
def regist_page(request):
    return render(request,'user/register.html')


@logs
def regist(request):
    username=request.POST.get('userid')
    password=request.POST.get('psw')
    password=make_password(password)
    phone=request.POST.get('usrtel')
    email=request.POST.get('email')
    TUser.objects.create(id=uuid.uuid4(),username=username,password=password,phone=phone,email=email)
    return HttpResponse('恭喜您，注册成功')
@logs
def code(request):
    username=request.POST.get('phone_num')
    phone_num = TUser.objects.filter(phone=username)
    if phone_num:
        a = random.randint(100000, 999999)
        __business_id = uuid.uuid1()
        # print(__business_id)
        # params = "{\"code\":\"12345\",\"product\":\"云通信\"}"
        params = u'{"code":"'+str(a)+'"}'
        print(send_sms(__business_id, username, "广告", "SMS_29435071", params))
        request.session['code2']=a
        return HttpResponse('短信已经发送')
    else:
        return HttpResponse('请注册手机号')

@logs
def phone(requset):
    a=requset.session.get('code2')
    code=requset.POST.get('code')
    print(a,code)
    if int(code)==int(a):
        return redirect('gl:sy')
    return HttpResponse('验证码错误')
