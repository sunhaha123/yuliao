# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Library(models.Model):
    pre_word = models.CharField(max_length=300,verbose_name=u'词前')
    word = models.CharField(max_length=300,verbose_name=u'单词')
    after_word = models.CharField(max_length=300, verbose_name=u'词前')
    source = models.CharField(max_length=30, verbose_name=u'出处', default="")
    # birthday = models.DateField(null=True, blank=True, verbose_name=u'生日', default='2010-01-01')
    # is_staff = models.BooleanField(default=False,verbose_name=u'是否为老师')

    class Meta:
        verbose_name = u'语料库'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.word