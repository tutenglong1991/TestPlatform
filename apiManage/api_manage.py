#!/usr/bin/env python
# -*-coding:utf-8-*-

from .models import ApiSet, ApiParameters
import datetime
import time
import json


class ApiManage:

    def add_api(self, **resp):
        for key in resp:
            dict_key = json.loads(key)

        api_add_data = {'apiName': dict_key['apiName'], 'apiPath': dict_key['apiPath'],
                        'apiDomain': dict_key['apiDomain'], 'netProtocol': dict_key['netProtocol'],
                        'reqMethods': dict_key['reqMethods'], 'reqUa': dict_key['reqUa'], 'ownPro': dict_key['ownPro'],
                        'ownGroup': dict_key['ownGroup'], 'runStatus': dict_key['runStatus']}
        try:
            # 插入接口信息到接口表
            api_add_data_obj = ApiSet(**api_add_data)
            api_add_data_obj.save()
            # 只有接口插入成功后，才能再循环插入接口下的参数
            api_params_list = dict_key['parameters']
            for param in api_params_list:
                api_params_data_objs = {'paramName': param['paramName'],
                                        'paramValue': param['paramValue'],
                                        'isForce': param['isForce'],
                                        'paramType': param['paramType'],
                                        'paramRemark': param['paramRemark']}
                api_params_add_data_obj = ApiParameters(**api_params_data_objs)
                # 外键插入（ownApi_id），即将添加接口和输入的参数关联
                api_params_add_data_obj.ownApi_id = ApiSet.objects.values('id').filter(apiName=dict_key['apiName'])[0]['id']
                api_params_add_data_obj.save()
            # 通过relate_name查询主键中某个值与外键关联表中的数据
            # ownApi = ApiSet.objects.values('id').filter(apiName=dict_key['apiName'])[0]['id']
            # api = ApiSet.objects.get(id=ownApi['id'])
            # param = api.api_params.values_list()
            msg = '添加接口和参数成功'
            return {'status': 200, 'msg': msg}
        except Exception as e:
            error = str(e)
            print(error)
            if error.__contains__('UNIQUE '):
                msg = '接口已存在，请重新输入接口或去详情编辑接口'
            elif error.__contains__('NULL'):
                msg = '存在必填参数未填写，请检查后再提交'
            return {'status': 500, 'msg': msg}


if __name__ == '__main__':
    API = ApiManage()
