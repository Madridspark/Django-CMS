# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.urlresolvers import reverse

@python_2_unicode_compatible
class StaticInfo(models.Model):
    theName = models.CharField('本站名称', max_length=256)
    theLink = models.CharField('本站网址', max_length=256)
    theLogo = models.FileField('Logo', upload_to='./central/logo-file/')
    theIntro = models.TextField('本站简介', default='')
    theVisits = models.IntegerField('访问量')
    theSigners = models.IntegerField('注册量')
    thePartners = models.IntegerField('合作伙伴数')
    theTEL = models.CharField('电话', max_length=256)
    theEmail = models.CharField('E-mail', max_length=256)
    theAddress = models.CharField('地址', max_length=256)
    thePostcode = models.CharField('邮编', max_length=256)

    def __str__(self):
        return self.theName

    class Meta:
        verbose_name = '本站信息'
        verbose_name_plural = '本站信息'


@python_2_unicode_compatible
class StaticTeammates(models.Model):
    thePersonName = models.CharField('名字', max_length=256)
    thePersonIntro = models.TextField('简介', default='')
    theHeaderImage = models.FileField('上传头像', upload_to='./central/header-image-files/')

    def __str__(self):
        return self.thePersonName

    class Meta:
        verbose_name = '团队成员'
        verbose_name_plural = '团队成员信息'


@python_2_unicode_compatible
class HeroImages(models.Model):
    theHeroTitle = models.CharField('标题', max_length=256, unique=True)
    theImage = models.FileField('上传文件', upload_to='./central/hero-image-files/')
    theLink = models.TextField('超链接', default='')
    
    def __str__(self):
        return self.theHeroTitle

    class Meta:
        verbose_name = '轮播图片'
        verbose_name_plural = '轮播图片的链接和文件名'

@python_2_unicode_compatible
class Page1Video(models.Model):
    theTitle = models.CharField('标题', max_length=256, unique=True)
    OGG = models.FileField('ogg', upload_to='./central/video-files/')
    MP4 = models.FileField('mp4', upload_to='./central/video-files/')
    WEBM = models.FileField('webm', upload_to='./central/video-files/')
    SWF = models.FileField('swf', upload_to='./central/video-files/')
    
    def __str__(self):
        return self.theTitle

    class Meta:
        verbose_name = '宣传视频'
        verbose_name_plural = '宣传视频'