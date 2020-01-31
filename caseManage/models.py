# coding=utf-8
from django.db import models


class CaseSet(models.Model):
    id = models.IntegerField(primary_key=True)  # 此处不能设置default，否则不是自增，是update
    caseName = models.CharField(max_length=200, unique=True, verbose_name='用例名称')
    caseLevel = models.CharField(max_length=5, verbose_name='用例级别')
    casePro = models.IntegerField(verbose_name='所属项目id')
    caseModule = models.CharField(max_length=200, verbose_name='所属模块')
    caseApi = models.IntegerField(verbose_name='所属接口id')
    caseRemark = models.CharField(max_length=500, verbose_name='用例备注信息')
    runStatus = models.IntegerField(default=0, verbose_name='用例执行状态，0：未执行, 1：通过，2：失败')
