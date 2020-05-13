#!/usr/bin/env python
# -*-coding:utf-8-*-

from .models import ApiSet, ApiParameters, CommonConf
from projectManage.models import Project
from .requestMain import runApiMain
import json
from .config import user
import datetime


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
            # caseSet = ApiSet.objects.get(id=ownApi['id'])
            # param = caseSet.api_params.values_list()
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
    def query_api_options(self, **resp):
        print(resp)
        if len(resp) == 0:
            sql = "select id, apiName, apiPath, apiModule from api_manage group by apiModule order by id ASC"
        else:
            project_id = int(resp['selected_pro'])
            sql = "select id, apiName, apiPath, apiModule from api_manage where ownPro='%d' group by apiModule order by id ASC" % project_id
        module_data_list = []
        api_data_list = []
        api_module_obj = dict()
        for A in ApiSet.objects.raw(sql):
            api_obj = {'value': A.apiName, 'label': A.apiPath}
            module_obj = {'value': A.apiModule, 'label': A.apiModule}
            module_data_list.append(module_obj)
            api_data_list.append(api_obj)
        api_module_obj['modules'] = module_data_list
        api_module_obj['api'] = api_data_list
        return api_module_obj

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

    # 插入及更新公共配置信息
    # def set_common_config(self, **resp):
    #     # 先处理入参
    #     for key in resp:
    #         dict_key = json.loads(key)
    #     api_common_cf = {'httpProtocol': dict_key['httpProtocol'], 'httpMethods': dict_key['httpMethods'],
    #                      'httpDomain': dict_key['httpDomain'], 'httpPath': dict_key['httpPath'],
    #                      'httpPort': dict_key['httpPort'], 'httpHeader': dict_key['httpHeader'],
    #                      'userDefinedVar': dict_key['userDefinedVar'], 'relApiList': dict_key['relApiList'],
    #                      'isForAllApi': dict_key['isForAllApi']}
    #     # 查询该表，若结果为空则执行插入语句
    #     apiConfig_querySet = CommonConf.objects.values_list().order_by('id')
    #     if len(apiConfig_querySet) == 0:
    #         try:
    #             # 插入配置信息到配置表格
    #             api_common_cf_obj = CommonConf(**api_common_cf)
    #             api_common_cf_obj.save()
    #             msg = '模板添加成功'
    #             return {'status': 200, 'msg': msg}
    #         except Exception as e:
    #             error = str(e)
    #             return {'status': 500, 'msg': error}
    #     else:
    #         try:
    #             # 先更新公共配置表中的信息
    #             apiConfig_querySet.update(**api_common_cf)
    #             # 再更新关联了使用当前公共配置接口中的相关字段，如httpProtocol，httpMethods等
    #             relApiList = api_common_cf['relApiList']
    #             isForAllApi = api_common_cf['isForAllApi']
    #             apiSetObj = dict()
    #             apiSetObj['netProtocol'] = api_common_cf['httpProtocol']
    #             apiSetObj['reqMethods'] = api_common_cf['httpMethods']
    #             apiSetObj['apiDomain'] = api_common_cf['httpDomain']
    #             apiSetObj['apiPath'] = api_common_cf['httpPath']
    #             apiSetObj['apiPort'] = api_common_cf['httpPort']
    #
    #             # 是否选择全部接口，1表示全部
    #             if isForAllApi == 1:
    #                 # 判断公共配置对象中的header设置项是否与接口对象中的header差异，若存在相同的key
    #                 # 则使用公共对象配置传入的value更新接口中该相同key的value值
    #                 # 若接口对象中没有的key，则接口对象新增改key
    #                 apiHeaderObj = ApiSet.objects.values_list()
    #                 for attr_obj in api_common_cf['httpHeader']:
    #                     apiHeaderObj.
    #                     if apiHeaderObj[attr_obj] is not None:
    #
    #
    #
    #
    #                 ApiSet.objects.values_list().update(**apiSetObj)
    #                 msg = '公共配置已经更新到全部接口'
    #                 return {'status': 200, 'msg': msg}
    #             else:
    #                 for apiId in relApiList:
    #                     ApiSet.objects.filter(id=apiId).values_list().update(**apiSetObj)
    #                 msg = '公共配置已经更新到所选择需要适用的接口'
    #                 return {'status': 200, 'msg': msg}
    #         except Exception as e:
    #             error = str(e)
    #             return {'status': 500, 'msg': error}

    def edit_api(self, **resp):
        for key in resp:
            dict_key = json.loads(key)
        params = dict_key['parameters']
        dict_key.pop('parameters')
        # 如果参数为空，接口无任何入参，则只更新接口
        if len(params) == 0:
            ApiSet.objects.filter(id=dict_key['id']).values_list().update(**dict_key)
            msg = "接口更新成功"
        else:
            # 先更新接口，再更新接口下的参数
            ApiSet.objects.filter(id=dict_key['id']).values_list().update(**dict_key)
            for pa in params:
                # 若参数无id则为新增参数，调用数据库模型插入保存方法
                if pa['id'] is None:
                    pa.pop('id')
                    ApiParameters(**pa).save()
                    msg = '更新接口，添加参数成功'
                else:
                    try:
                        _t = ApiParameters.objects.filter(id=pa['id']).values_list()
                        if _t:
                            _t.update(**pa)
                            msg = '更新接口，修改参数成功'
                        else:
                            msg = '更新接口，修改参数失败'
                    except Exception as e:
                        print(e)
                        msg = '更新接口成功，修改参数失败'
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
        if len(user['cookies']) == 0:
            # 调登录接口获取cookies并保存
            cookies = rAm.login_GBT()
            user['cookies'] = cookies.get_dict()
            user['lastLoginTime'] = datetime.datetime.now()
        else:
            newLoginTime = datetime.datetime.now()
            timeGap = (newLoginTime - user['lastLoginTime']).seconds
            # 若已存在cookies，且cookies无效(暂时设置3h重新获取一次)
            if timeGap >= 10800:
                # 再调登录接口重新获取cookies并保存
                cookies = rAm.login_GBT()
                user['cookies'] = cookies.get_dict()
                user['lastLoginTime'] = newLoginTime
            else:
                # 若已存在cookies，且cookies还有效，则将原来的cookies赋值给最新的会话
                rAm.session.cookies.update(user['cookies'])
        print(dict_key)
        print(dict_key['reqUa'].replace('"', "'"))
        default_headers = json.loads(dict_key['reqUa'])
        if len(req_param_data) == 0:
            req_param_data = None
        api_obj = ApiSet.objects.filter(id=dict_key['id'])
        runParam = json.dumps(req_param_data)
        try:
            runResp = rAm.run_main(methods, req_param_url, req_data=req_param_data, headers=default_headers)
            runResp_dict = json.loads(runResp)
            format_runResp = json.dumps(runResp_dict, indent=4, sort_keys=True, ensure_ascii=False)
            if runResp_dict['code'] == 0:
                api_obj.update(runStatus=1)
                status = 200
                msg = '接口运行成功'
            else:
                api_obj.update(runStatus=2)
                status = 500
                msg = '接口运行失败'
        except Exception as e:
            api_obj.update(runStatus=2)
            status = 500
            msg = '接口运行失败'
        return {'status': status, 'msg': msg, 'runResp': format_runResp, 'runParam': runParam}

    def del_api(self):
        pass


if __name__ == '__main__':
    API = ApiManage()
