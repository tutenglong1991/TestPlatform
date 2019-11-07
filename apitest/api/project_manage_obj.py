#!/usr/bin/env python
# -*-coding:utf-8-*-

from apitest.models import *
import datetime


def find_project(**resp):
    """ 查找项目 """
    pro_name = resp['projectName']
    query_result = {}
    project_data = []
    if pro_name == '':
        pro_queryset = Project.objects.all().values_list('id', 'proname', 'current_host', 'principal',
                                                         'created_time', 'update_time').order_by('id')
    else:
        pro_queryset = Project.objects.filter(proname=pro_name).values_list('id', 'proname', 'current_host',
                                                                            'principal', 'created_time',
                                                                            'update_time')
    for qs in pro_queryset:
        project_datas = dict()
        project_datas['id'] = qs[0]
        project_datas['proname'] = qs[1]
        project_datas['current_host'] = qs[2]
        project_datas['principal'] = qs[3]
        project_datas['created_time'] = datetime.datetime.strftime(qs[4], "%Y-%m-%d %H:%M:%S")
        project_datas['update_time'] = datetime.datetime.strftime(qs[5], "%Y-%m-%d %H:%M:%S")
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
    """ 返回待编辑项目信息 """
    pro_id = resp['id']
    _edit = Project.objects.filter(id=pro_id).values_list('id', 'proname', 'current_host', 'principal')
    _edit_data = {
        'id': _edit[0][0],
        'proname': _edit[0][1],
        'current_host': _edit[0][2],
        'principal': _edit[0][3]
    }
    return _edit_data


def update_pro(**resp):
    try:
        _t = Project.objects.filter(proname=resp['proname'])
        if _t:
            _t.__dict__.update(**resp)
            _t.save()
            msg = '更新项目数据数据成功'
        else:
            """添加项目"""
            pro_data = {'proname': resp['proname'], 'current_host': resp['current_host'],
                        'principal': resp['principal']}
            create_pro_data = Project(**pro_data)
            create_pro_data.save()
            msg = '添加项目成功'
    except Exception as e:
        msg = '更新项目数据失败,请联系管理员'
    return {'status': 500, 'data': msg}


def del_pro(**resp):
    pro_id = resp['id']
    try:
        Project.objects.filter(id=pro_id).delete()
        msg = '删除数据成功'
    except Exception as e:
        msg = '删除数据失败，请联系管理员'
    return {'status': 500, 'data': msg}


class ProjectManage:
    pass
