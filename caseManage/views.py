#!/usr/bin/env python
# -*-coding:utf-8-*-

from caseManage.case_manage import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from caseManage.run_tests import caseRunnerObj


@csrf_exempt
def case_manage(request, operate):
    # 实例化用例管理类
    caseMa = caseManage()
    # 实例化用例执行类
    caseRu = caseRunnerObj()
    case_data = {}
    if request.method == "POST":
        resp = request.POST.dict()
        try:
            if operate == 'addCase':
                case_data = caseMa.add_case(**resp)
            # 手动触发执行用例
            elif operate == 'manualRunCase':
                case_data = caseRu.manualRunCase(**resp)
            return JsonResponse({"code": 200, "data": case_data})
        except Exception as e:
            print(e)
            return JsonResponse({"code": 500, "msg": e})
    else:
        resp = request.GET.dict()
        try:
            if operate == 'caseList':
                case_data = caseMa.query_case(**resp)
            elif operate == 'options-apiModule':
                case_data = caseMa.query_module_apis(**resp)
            return JsonResponse({"code": 200, "data": case_data})
        except Exception as e:
            print(e)
            return JsonResponse({"code": 500, "msg": "服务内部异常，请联系管理员"})
