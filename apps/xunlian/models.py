# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from yundongyuan.models import Athlete
from events.models import Xiangmu

# Create your models here.
class XunlianDate(models.Model):
    xingming = models.ForeignKey(Athlete, verbose_name=u'队员姓名')
    riqi = models.DateField(null=True, blank=True, verbose_name=u'训练日期', default='2010-01-01')
    xiangmu = models.ForeignKey(Xiangmu, verbose_name=u'体操项目')
    # gender = models.CharField(max_length=6, choices=(("male", u"男"), ("female", u"女")), default=u"male",
    #                           verbose_name=u'性别')
    # address = models.CharField(max_length=100, default=u'', verbose_name=u'地址')
    # mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name=u'手机号')



    class Meta:
        verbose_name = u'训练记录'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.xingming.name


class XunlianSh(models.Model):
    xingming = models.ForeignKey(Athlete, verbose_name=u'队员姓名')
    riqi = models.DateField(null=True, blank=True, verbose_name=u'训练日期', default='2010-01-01')
    gaotong = models.FloatField(verbose_name=u'睾酮')
    # gender = models.CharField(max_length=6, choices=(("male", u"男"), ("female", u"女")), default=u"male",
    #                           verbose_name=u'性别')
    # address = models.CharField(max_length=100, default=u'', verbose_name=u'地址')
    # mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name=u'手机号')



    class Meta:
        verbose_name = u'训练-生化'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.xingming.name