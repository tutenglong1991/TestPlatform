#!/usr/bin/env python
# -*-coding:utf-8-*-


from django.urls import path
from apitest import views

urlpatterns = [
    path('/projectList/<operate>', views.project_manage)
]