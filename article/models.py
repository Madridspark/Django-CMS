# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.urlresolvers import reverse

@python_2_unicode_compatible
class Column(models.Model):
    name = models.CharField('栏目名称', max_length=256)
    link = models.CharField('栏目链接', max_length=256, db_index=True)
    intro = models.TextField('栏目简介', default='')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('column', args=(self.link,))

    class Meta:
        verbose_name = '栏目'
        verbose_name_plural = '栏目'
        ordering = ['name']

@python_2_unicode_compatible
class Article(models.Model):
    title = models.CharField('文章标题', max_length=256)
    link = models.CharField('文章链接', max_length=256, db_index=True)

    author = models.ForeignKey('auth.User', blank=True, null=True, verbose_name='作者')
    content = models.TextField('内容', default='', blank=True)

    column = models.ManyToManyField(Column, verbose_name='归属栏目')
    pub_time = models.DateField('发布时间', auto_now_add=True, editable=True)
    update_time = models.DateField('更新时间', auto_now=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article', args=(self.pk, self.link))

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'
