# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Sport(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"运动英文名称")
    c_name = models.CharField(max_length=50, verbose_name=u"运动中文名称")



    class Meta:
        verbose_name = u'运动项目信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name