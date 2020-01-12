#!/usr/bin/env python
# -*-coding:utf-8-*-

from apiManage.api_manage import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def api_manage(request, operate):
    api = ApiManage()
    api_data = {}
    if request.method == "POST":
        resp = request.POST.dict()
        try:
            if operate == 'addApi':
                api_data = api.add_api(**resp)
            elif operate == 'editApi':
                api_data = api.edit_api(**resp)
            elif operate == 'delApi':
                api_data = api.del_api(**resp)
            elif operate == 'runApi':
                api_data = api.run_api(**resp)
            code = api_data['status']
            return JsonResponse({"code": code, "data": api_data})
        except Exception as e:
            print(e)
            return JsonResponse({"code": 500, "msg": e})
    else:
        resp = request.GET.dict()
        try:
            if operate == 'apiList':
                api_data = api.query_apiInfo(**resp)
            elif operate == 'options-apiModule':
                api_data = api.query_api_options()
            elif operate == 'parameterOfApi':
                api_data = api.query_api_params(**resp)
            return JsonResponse({"code": 200, "data": api_data})
        except Exception as e:
            print(e)
            return JsonResponse({"code": 500, "msg": "查找项目失败"})
