#!/usr/bin/env python
# -*-coding:utf-8-*-

# from apitest.api.project_manage_obj import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def project_manage(request, operate):
	resp = request.POST.dict()
	print(resp)
	# if operate == 'find':
	# 	pro_data = find_project(**resp)
	# elif operate == 'editPro':
	# 	pro_data = edit_pro(**resp)
	# elif operate == 'updatePro':
	# 	pro_data = update_pro(**resp)
	# elif operate == 'delPro':
	# 	resp_get = request.POST.dict()
	# 	print(resp_get)
	# 	pro_data = del_pro(**resp_get)
	return JsonResponse({"pro_data": "test"})