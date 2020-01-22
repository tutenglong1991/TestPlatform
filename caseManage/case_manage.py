#!/usr/bin/env python
# -*-coding:utf-8-*-

from apiManage.requestMain import runApiMain
from apiManage.models import ApiSet, ApiParameters


class caseManage:

    def add_case(self):
        pass

    def query_case(self, **resp):
        case_queryResult_list = []
        print(resp)
        print(len(resp))
        # if len(resp) == 0:
        #     apiList_querySet = ApiSet.objects.values_list().order_by('id').reverse()
        # else:
        #     apiList_querySet = ApiSet.objects.filter(**resp).values_list()
        return case_queryResult_list

    def query_module_apis(self, **resp):
        print(resp)
        if len(resp) == 0:
            sql = "select id, apiName, apiModule from api_manage group by apiModule order by id ASC"
        else:
            project_id = int(resp['selected_pro'])
            sql = "select id, apiName, apiModule from api_manage where ownPro='%d' group by apiModule order by id ASC" % project_id
        api_module_combination_list = []
        for m in ApiSet.objects.raw(sql):
            module_obj = {'value': m.apiModule, 'label': m.apiModule, 'children': []}
            for an in ApiSet.objects.values().filter(apiModule=m.apiModule):
                module_obj['children'].append({'value': an['apiName'], 'label': an['apiName']})
            api_module_combination_list.append(module_obj)
        return api_module_combination_list
