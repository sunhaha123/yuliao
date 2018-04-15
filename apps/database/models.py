# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Library3(models.Model):
    pre_word = models.CharField(max_length=300,verbose_name=u'词前')
    word = models.CharField(max_length=300,verbose_name=u'单词')
    after_word = models.CharField(max_length=300, verbose_name=u'词前')
    source = models.CharField(max_length=30, verbose_name=u'出处',default=u'null')
    meaning = models.CharField(max_length=30, verbose_name=u'关键词语义',default=u'null')
    partofspeech = models.CharField(max_length=30, verbose_name=u'关键词词性',default=u'null')
    cexing = models.CharField(max_length=30, verbose_name=u'层性',default=u'null')
    BCcengxing = models.CharField(max_length=30, verbose_name=u'表层层性',default=u'null')



    class Meta:
        verbose_name = u'语料库'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.word