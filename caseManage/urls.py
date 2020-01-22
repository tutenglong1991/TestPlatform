#!/usr/bin/env python
# -*-coding:utf-8-*-


from django.urls import path
from caseManage import views

urlpatterns = [
    path('<operate>', views.case_manage)
]
