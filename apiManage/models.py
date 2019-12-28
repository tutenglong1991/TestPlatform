# coding=utf-8
from django.db import models


class ApiSet(models.Model):
    id = models.IntegerField(primary_key=True)  # 此处不能设置default，否则不是自增，是update
    apiName = models.CharField(max_length=200, unique=True, verbose_name='接口名称')
    apiPath = models.CharField(max_length=1024, verbose_name='接口地址')
    apiDomain = models.CharField(max_length=512, verbose_name='域名或ip')
    netProtocol = models.IntegerField(verbose_name='网络协议，0为http，1为https')
    reqMethods = models.IntegerField(verbose_name='请求方式，0为get，1为post')
    reqUa = models.CharField(max_length=200, null=True, verbose_name='域名或ip')
    apiModule = models.CharField(max_length=200, verbose_name='所属模块')
    ownPro = models.CharField(max_length=200, verbose_name='项目ID')
    runStatus = models.IntegerField(default=0, verbose_name='接口执行状态，0：未执行，1：成功，2：失败')

    class Meta:
        db_table = 'api_manage'  # 数据库表名
        verbose_name = u'接口名称'  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称
        ordering = ['id']


class ApiParameters(models.Model):
    id = models.IntegerField(primary_key=True)
    ownApi = models.ForeignKey(to='ApiSet', to_field='id', related_name='api_params', on_delete=models.SET_NULL, blank=True, null=True,)
    paramName = models.CharField(max_length=200, verbose_name='参数名称')
    paramValue = models.CharField(max_length=200, null=True, verbose_name='参数值')
    isForce = models.CharField(max_length=1, verbose_name='是否必选')
    paramType = models.CharField(max_length=20, verbose_name='参数类型')
    paramRemark = models.CharField(max_length=4096, null=True, verbose_name='参数注释，或实例')

    class Meta:
        db_table = 'api_parameters'  # 数据库表名
        verbose_name = u'参数名称'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return self.paramName
