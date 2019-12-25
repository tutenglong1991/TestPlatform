#!/usr/bin/env python
# -*-coding:utf-8-*-

from apiManage.api_manage import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def api_manage(request, operate):
    print(operate)
    api = ApiManage()
    if request.method == "POST":
        resp = request.POST.dict()
        try:
            if operate == 'addApi':
                pro_data = api.add_api(**resp)
            elif operate == 'editApi':
                pro_data = api.edit_api(**resp)
            elif operate == 'delApi':
                pro_data = api.del_api(**resp)
            return JsonResponse({"code": 200, "data": pro_data})
        except Exception as e:
            print(e)
            return JsonResponse({"code": 500, "msg": e})
    else:
        resp = request.GET.dict()
        try:
            if operate == 'apiList':
                pro_data = api.query_apis(**resp)
            return JsonResponse({"code": 200, "data": pro_data})
        except Exception as e:
            print(e)
            return JsonResponse({"code": 500, "msg": "查找项目失败"})
