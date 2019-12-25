#!/usr/bin/env python
# -*-coding:utf-8-*-


from django.urls import path
from apiManage import views

urlpatterns = [
    path('<operate>', views.api_manage)
]