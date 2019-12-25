#!/usr/bin/env python
# -*-coding:utf-8-*-

from apiManage.models import *
import datetime
import time
import json


class ApiManage:

    def add_api(self, **resp):
        print('test')
        # for key in resp:
        #     dict_key = json.loads(key)
        # projectCycle_list = dict_key['projectCycle']
        # pro_add_data = {'projectName': dict_key['projectName'], 'projectType': dict_key['projectType'],
        #                 'dept': dict_key['dept'], 'code': dict_key['code'], 'productLine': dict_key['productLine'],
        #                 'projectStartTime': projectCycle_list[0], 'projectEndTime': projectCycle_list[1],
        #                 'status': dict_key['status'], 'creator': dict_key['creator']}
        # pro_add_data_obj = Project(**pro_add_data)
        # pro_add_data_obj.save()
        msg = '添加项目成功'
        return {'status': 200, 'msg': msg}


if __name__ == '__main__':
    API = ApiManage()
