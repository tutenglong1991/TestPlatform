#!/usr/bin/env python
# -*-coding:utf-8-*-

from projectManage.project_manage_obj import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def project_manage(request, operate):
    PM = ProjectManage()
    if request.method == "POST":
        resp = request.POST.dict()
        try:
            if operate == 'addPro':
                pro_data = PM.add_project(**resp)
            elif operate == 'editPro':
                pro_data = PM.edit_pro(**resp)
            elif operate == 'delPro':
                pro_data = PM.del_pro(**resp)
            return JsonResponse({"code": 200, "data": pro_data})
        except Exception as e:
            print(e)
            return JsonResponse({"code": 500, "msg": e})
    else:
        resp = request.GET.dict()
        if operate == 'find':  # 如果查询项目接口未传任何参数，则不需要处理入参
            try:
                pro_data = PM.find_project(**resp)
                return JsonResponse({"code": 200, "data": pro_data})
            except Exception as e:
                print(e)
                return JsonResponse({"code": 500, "msg": "查找项目失败"})
