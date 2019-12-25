#!/usr/bin/env python
# -*-coding:utf-8-*-


from django.urls import path
from projectManage import views

urlpatterns = [
    path('projectList/<operate>', views.project_manage),
]