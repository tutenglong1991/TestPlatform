#!/usr/bin/env python
# -*-coding:utf-8-*-

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from functools import wraps


def is_admin(adminAccount, adminPwd):
    def admin_decorator(func):
        @wraps(func)
        def wrapper(request):
            resp = request.POST.dict()
            for k in resp:
                account = json.loads(k)["account"]
                password = json.loads(k)["password"]
            if adminAccount == account and adminPwd == password:
                print("我是管理员")
                wrapper_admin = True
            else:
                print("我不是管理员")
                wrapper_admin = False
            return func(request, wrapper_admin)

        return wrapper

    return admin_decorator


@csrf_exempt
@is_admin('hemeilong', '12345678')  # 自定义验证是否是管理员身份登录的装饰器测试，可在登录之前进行前置验证
def login(request, admin=False):
    # resp = request.POST.dict()
    # for k in resp:
    #     account = json.loads(k)["account"]
    #     password = json.loads(k)["password"]
    print("我是登录接口")
    if admin:
        return JsonResponse({"code": 200, "message": "欢迎光临，登录成功"})
    else:
        return JsonResponse({"code": 500, "message": "用户名或密码错误"})
