#!/usr/bin/env python
# -*-coding:utf-8-*-

from .models import ApiSet, ApiParameters
from projectManage.models import Project
from .requestMain import runApiMain
import json


class ApiManage:

    def add_api(self, **resp):
        for key in resp:
            dict_key = json.loads(key)

        api_add_data = {'apiName': dict_key['apiName'], 'apiPath': dict_key['apiPath'],
                        'apiDomain': dict_key['apiDomain'], 'netProtocol': dict_key['netProtocol'],
                        'reqMethods': dict_key['reqMethods'], 'reqUa': dict_key['reqUa'], 'ownPro': dict_key['ownPro'],
                        'apiModule': dict_key['apiModule'], 'runStatus': dict_key['runStatus']}
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
                api_params_add_data_obj.ownApi_id = ApiSet.objects.values('id').filter(apiName=dict_key['apiName'])[0][
                    'id']
                api_params_add_data_obj.save()
            # 通过relate_name查询主键中某个值与外键关联表中的数据
            # ownApi = ApiSet.objects.values('id').filter(apiName=dict_key['apiName'])[0]['id']
            # api = ApiSet.objects.get(id=ownApi['id'])
            # param = api.api_params.values_list()
            msg = '添加接口和参数成功'
            return {'status': 200, 'msg': msg}
        except Exception as e:
            error = str(e)
            if error.__contains__('UNIQUE '):
                msg = '接口已存在，请重新输入接口或去详情编辑接口'
            elif error.__contains__('NULL'):
                msg = '存在必填参数未填写，请检查后再提交'
            return {'status': 500, 'msg': msg}

    # 仅查询接口名称和所属的模块数据，用于下拉选项
    def query_api_options(self):
        api_data_list = []
        api_options_querySet = ApiSet.objects.values('id', 'apiName', 'apiPath', 'apiModule').order_by('id').reverse()
        for qs in api_options_querySet:
            api_datas_obj = dict()
            api_datas_obj['id'] = qs['id']
            api_datas_obj['apiName'] = qs['apiName']
            api_datas_obj['apiPath'] = qs['apiPath']
            api_datas_obj['apiModule'] = qs['apiModule']
            api_data_list.append(api_datas_obj)
        return api_data_list

    # 查询接口全部数据,用于接口列表展示
    def query_apiInfo(self, **resp):
        apiList_result_list = []
        if len(resp) == 0:
            apiList_querySet = ApiSet.objects.values_list().order_by('id').reverse()
        else:
            apiList_querySet = ApiSet.objects.filter(**resp).values_list()
        for apiTuple_querySet in apiList_querySet:
            apiList_result = dict()  # 此处必须每次循环重新生成一个字段对象用来保存一条接口信息，若在外面定义则是重新赋值
            apiList_result['id'] = apiTuple_querySet[0]
            apiList_result['apiName'] = apiTuple_querySet[1]
            apiList_result['apiPath'] = apiTuple_querySet[2]
            apiList_result['apiDomain'] = apiTuple_querySet[3]
            if apiTuple_querySet[4] == 0:
                apiList_result['netProtocol'] = 'http'
            elif apiTuple_querySet[4] == 1:
                apiList_result['netProtocol'] = 'https'
            if apiTuple_querySet[5] == 0:
                apiList_result['reqMethods'] = 'get'
            elif apiTuple_querySet[5] == 1:
                apiList_result['reqMethods'] = 'post'
            apiList_result['reqUa'] = apiTuple_querySet[6]
            apiList_result['apiModule'] = apiTuple_querySet[7]
            ownProName = Project.objects.values('projectName').filter(id=apiTuple_querySet[8])
            apiList_result['ownPro'] = ownProName[0]['projectName']
            if apiTuple_querySet[9] == 0:
                apiList_result['runStatus'] = '未执行'
            elif apiTuple_querySet[9] == 1:
                apiList_result['runStatus'] = '成功'
            elif apiTuple_querySet[9] == 2:
                apiList_result['runStatus'] = '失败'
            apiList_result_list.append(apiList_result)
        return apiList_result_list

    # 编辑接口时查询接口下的参数，供回写
    def query_api_params(self, **resp):
        param_querySet = ApiParameters.objects.values_list().filter(ownApi_id=resp['id'])
        param_list = []
        for param in param_querySet:
            print(param)
            param_obj = dict()
            param_obj['id'] = param[0]
            param_obj['paramName'] = param[2]
            param_obj['paramValue'] = param[3]
            param_obj['isForce'] = param[4]
            param_obj['paramType'] = param[5]
            param_obj['paramRemark'] = param[6]
            param_obj['ownApi_id'] = param[1]
            param_list.append(param_obj)
        return param_list

    def edit_api(self, **resp):
        for key in resp:
            dict_key = json.loads(key)
        print(dict_key)
        params = dict_key['parameters']
        dict_key.pop('parameters')
        ApiSet.objects.filter(id=dict_key['id']).values_list().update(**dict_key)
        for pa in params:
            print(pa)
            if pa['id'] is None:
                pa.pop('id')
                ApiParameters(**pa).save()
                msg = '添加参数成功'
            else:
                try:
                    _t = ApiParameters.objects.filter(id=pa['id']).values_list()
                    if _t:
                        _t.update(**pa)
                        msg = '修改参数成功'
                    else:
                        msg = '修改参数失败'
                except Exception as e:
                    print(e)
                    msg = '修改参数失败'
        return {'status': 200, 'msg': msg}

    def run_api(self, **resp):
        for key in resp:
            dict_key = json.loads(key)
        reqMethods = dict_key['reqMethods']
        netProtocol = dict_key['netProtocol']
        if reqMethods == 0:
            methods = 'get'
        else:
            methods = 'post'
        if netProtocol == 0:
            net = 'http'
        else:
            net = 'https'
        apiDomain = dict_key['apiDomain']
        apiPath = dict_key['apiPath']
        param_list = dict_key['parameters']
        req_param_data = dict()
        for param in param_list:
            paramType = param['paramType']
            # 此处参数类型由字符串转换成其他各种类型后续再补充
            if paramType == 'Int':
                req_param_data[param['paramName']] = int(param['paramValue'])
            elif paramType == 'float':
                req_param_data[param['paramName']] = float(param['paramValue'])
            elif paramType == 'String':
                req_param_data[param['paramName']] = param['paramValue']
        req_param_url = net + '://' + apiDomain + apiPath

        rAm = runApiMain()
        cookies = rAm.login_GBT()
        print(type(cookies.get_dict()))
        default_headers = json.loads(dict_key['reqUa'])
        if len(req_param_data) == 0:
            req_param_data = None
        api_obj = ApiSet.objects.filter(id=dict_key['id'])
        try:
            print(req_param_data)
            runResp = rAm.run_main(methods, req_param_url, req_data=req_param_data, headers=default_headers)
            runResp_dict = json.loads(runResp)
            if runResp_dict['code'] == 0:
                api_obj.update(runStatus=1)
            else:
                api_obj.update(runStatus=2)
        except Exception as e:
            api_obj.update(runStatus=2)
        msg = '接口运行成功'
        runParam = json.dumps(req_param_data)
        return {'status': 200, 'msg': msg, 'runResp': runResp, 'runParam': runParam}

    def del_api(self):
        pass


if __name__ == '__main__':
    API = ApiManage()
