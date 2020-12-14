"""Gearbest_GBO_AutoTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    选推服务. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    选推服务. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    选推服务. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'homeLogin', TemplateView.as_view(template_name="index.html")),
    path('apiAutoTest/projectManage/', include('projectManage.urls')),
    path('login', include('login.urls')),
    path('apiAutoTest/apiInfo/', include('apiManage.urls')),
    path('apiAutoTest/caseInfo/', include('caseManage.urls')),
    #以下配置都是针对前端路由而非接口映射到后端后没有相应的url匹配规则，django报错配置，暂时使用改笨重的配置方法，后续再深入了解行业通用处理
    re_path(r'performanceAuto/mainHeader/autoPressMonitorJMeter', TemplateView.as_view(template_name="index.html")),
    re_path(r'performanceAuto/mainHeader/autoPressMonitorService', TemplateView.as_view(template_name="index.html")),
    re_path(r'continuousIntegration/mainHeader/ci', TemplateView.as_view(template_name="index.html")),
    re_path(r'functionAuto/mainHeader/projectManage', TemplateView.as_view(template_name="index.html")),
    re_path(r'functionAuto/mainHeader/projectMembers', TemplateView.as_view(template_name="index.html")),
    re_path(r'functionAuto/mainHeader/apiList', TemplateView.as_view(template_name="index.html")),
    re_path(r'functionAuto/mainHeader/apiAddPage', TemplateView.as_view(template_name="index.html")),
    re_path(r'functionAuto/mainHeader/updateRecord', TemplateView.as_view(template_name="index.html")),
    re_path(r'functionAuto/mainHeader/configList', TemplateView.as_view(template_name="index.html")),
    re_path(r'functionAuto/mainHeader/commonConfig', TemplateView.as_view(template_name="index.html")),
    re_path(r'functionAuto/mainHeader/apiDetail', TemplateView.as_view(template_name="index.html")),
    re_path(r'functionAuto/mainHeader/apiRunLog', TemplateView.as_view(template_name="index.html")),
    re_path(r'functionAuto/mainHeader/caseList', TemplateView.as_view(template_name="index.html")),
    re_path(r'functionAuto/mainHeader/caseDetail', TemplateView.as_view(template_name="index.html")),
    re_path(r'functionAuto/mainHeader/taskList', TemplateView.as_view(template_name="index.html")),
    re_path(r'functionAuto/mainHeader/taskRunLog', TemplateView.as_view(template_name="index.html")),
    re_path(r'functionAuto/mainHeader/programList', TemplateView.as_view(template_name="index.html")),
    re_path(r'functionAuto/mainHeader/reportList', TemplateView.as_view(template_name="index.html")),
    re_path(r'functionAuto/mainHeader/reportDetail', TemplateView.as_view(template_name="index.html")),
]
