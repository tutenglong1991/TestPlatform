#!/usr/bin/env python
# -*-coding:utf-8-*-


from django.urls import path
from apitest import views

urlpatterns = [
    path('project/<operate>/', views.project_manage)
]