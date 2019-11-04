#!/usr/bin/env python
# -*-coding:utf-8-*-

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def login(request):
    resp = request.POST.dict()
    for k in resp:
        account = json.loads(k)["account"]
        password = json.loads(k)["password"]
        if account == 'hemeilong' and password == '12345678':
            return JsonResponse({"code": 200, "message": "欢迎光临，登录成功"})
        else:
            return JsonResponse({"code": 101, "message": "用户名或密码错误"})
