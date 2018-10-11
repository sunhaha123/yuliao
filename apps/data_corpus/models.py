# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from  sports.models import Sport

# Create your models here.
class Library(models.Model):
    pre_word = models.CharField(max_length=300,verbose_name=u'词前')
    word = models.CharField(max_length=300,verbose_name=u'关键词')
    after_word = models.CharField(max_length=300, verbose_name=u'词后')
    source = models.CharField(max_length=30, verbose_name=u'出处',default=u'null')
    meaning = models.CharField(max_length=30, verbose_name=u'关键词语义',default=u'null')
    partofspeech = models.CharField(max_length=30, verbose_name=u'关键词词性',default=u'null')
    sport = models.ForeignKey(Sport,verbose_name=u'运动种类')
    cixing = models.CharField(max_length=30, verbose_name=u'层性',default=u'null')
    BCcengxing = models.CharField(max_length=30, verbose_name=u'表层层性',default=u'null')



    class Meta:
        verbose_name = u'语料'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.word