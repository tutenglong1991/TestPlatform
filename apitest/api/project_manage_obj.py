#!/usr/bin/env python
# -*-coding:utf-8-*-

from apitest.models import *
import datetime
import json


def add_project(**resp):
    for key in resp:
        dict_key = json.loads(key)
    projectCycle_list = dict_key['projectCycle']
    pro_add_data = {'projectName': dict_key['projectName'], 'projectType': dict_key['projectType'],
                    'dept': dict_key['dept'], 'code': dict_key['code'], 'productLine': dict_key['productLine'],
                    'projectStartTime': projectCycle_list[0], 'projectEndTime': projectCycle_list[1],
                    'status': dict_key['status'], 'creator': dict_key['creator']}
    print(type(pro_add_data))
    pro_add_data_obj = Project(**pro_add_data)
    pro_add_data_obj.save()
    msg = '添加项目成功'
    return {'status': 200, 'msg': msg}


def find_project(**resp):
    """ 查找项目 """
    query_result = {}
    project_data = []
    sql_params = {}
    for key in resp:
        if resp[key] == '':
            continue
        else:
            sql_params[key] = resp[key]
    if len(sql_params) == 0:
        pro_queryset = Project.objects.values_list().order_by('update_time').reverse()
    else:
        pro_queryset = Project.objects.filter(**sql_params).values_list()
    for qs in pro_queryset:
        project_datas = dict()
        project_datas['id'] = qs[0]
        project_datas['projectName'] = qs[1]
        project_datas['projectType'] = qs[2]
        project_datas['dept'] = qs[3]
        project_datas['code'] = qs[4]
        project_datas['productLine'] = qs[5]
        if qs[6] == '1':
            project_datas['status'] = '进行中'
        elif qs[6] == '0':
            project_datas['status'] = '已结束'
        elif qs[6] == '2':
            project_datas['status'] = '未开始'
        project_datas['creator'] = qs[7]
        project_datas['projectCycle'] = qs[8] + '-' + qs[9]
        project_datas['created_time'] = datetime.datetime.strftime(qs[10], "%Y-%m-%d %H:%M:%S")
        project_datas['update_time'] = datetime.datetime.strftime(qs[11], "%Y-%m-%d %H:%M:%S")
        project_data.append(project_datas)
    query_result['data'] = project_data
    return query_result
    # page = data.get('page') if data.get('page') else 1
    # per_page = data.get('sizePage') if data.get('sizePage') else 10
    # user_data = [{'user_id': u.id, 'user_name': u.name} for u in User.query.all()]
    # if project_name:
    #     _data = Project.query.filter(Project.name.like('%{}%'.format(project_name))).all()
    #     total = len(_data)
    #     if not _data:
    #         return jsonify({'msg': '没有该项目', 'status': 0})
    # else:
    #     pagination = Project.query.order_by(Project.id.asc()).paginate(page, per_page=per_page, error_out=False)
    #     _data = pagination.items
    #     total = pagination.total
    # project = [{'id': c.id,
    #             'host': c.host,
    #             'name': c.name,
    #             'choice': c.environment_choice,
    #             'principal': User.query.filter_by(id=c.user_id).first().name,
    #             'host_two': c.host_two, 'host_three': c.host_three, 'host_four': c.host_four} for c in _data]
    # return jsonify({'data': project, 'total': total, 'status': 1, 'userData': user_data})


def edit_pro(**resp):
    for key in resp:
        dict_key = json.loads(key)
    projectCycle_list = dict_key['projectCycle']
    dict_key['projectStartTime'] =  projectCycle_list[0]
    dict_key['projectEndTime'] = projectCycle_list[1]
    dict_key.pop('projectCycle')
    try:
        _t = Project.objects.filter(id=dict_key['id']).values_list()
        if _t:
            _t.update(**dict_key)
            msg = '更新项目数据数据成功'
        else:
            msg = '编辑项目失败，未找到该项目'
    except Exception as e:
        print(e)
        msg = '更新项目数据失败,请联系管理员'
    return {'status': 200, 'data': msg}


def del_pro(**resp):
    for key in resp:
        dict_key = json.loads(key)
    try:
        print(resp)
        Project.objects.filter(id=dict_key['id']).delete()
        msg = '删除数据成功'
    except Exception as e:
        print(e)
        msg = '删除数据失败，请联系管理员'
    return {'status': 200, 'data': msg}
