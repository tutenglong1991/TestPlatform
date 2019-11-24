#!/usr/bin/env python
# -*-coding:utf-8-*-

from apitest.api.project_manage_obj import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def project_manage(request, operate):
    if request.method == "POST":
        resp = request.POST.dict()
        try:
            if operate == 'addPro':
                pro_data = add_project(**resp)
            elif operate == 'editPro':
                pro_data = edit_pro(**resp)
            elif operate == 'delPro':
                pro_data = del_pro(**resp)
            return JsonResponse({"code": 200, "data": pro_data})
        except Exception as e:
            return JsonResponse({"code": 500, "msg": e})
    else:
        resp = request.GET.dict()
        key = resp['selectedParamsKey']
        resp[key] = resp['selectedParamsValue']
        resp.pop('selectedParamsKey')
        resp.pop('selectedParamsValue')
        try:
            if operate == 'find':
                pro_data = find_project(**resp)
            return JsonResponse({"code": 200, "data": pro_data})
        except Exception as e:
            print(e)
            return JsonResponse({"code": 500, "msg": "查找项目失败"})
