# coding=utf-8
from django.db import models


class Project(models.Model):

    id = models.IntegerField(primary_key=True)  # 此处不能设置default，否则不是自增，是update
    proname = models.CharField(max_length=200, null=True, unique=True, verbose_name='项目名称')
    current_host = models.CharField(max_length=1024, null=True, verbose_name='当前环境')
    principal = models.CharField(max_length=200, null=True, verbose_name='负责人')
    created_time = models.DateTimeField(null=True, verbose_name=u'创建日期', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)
    
    def __str__(self):
        return self.proname
    
    class Meta:
        db_table = 'project_manage'  # 数据库表名
        verbose_name = u'项目名称'
        verbose_name_plural = u'项目管理表'
        ordering = ['-created_time']