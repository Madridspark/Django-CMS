# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from DjangoUeditor.models import UEditorField


@python_2_unicode_compatible
class StaticInfo(models.Model):
    theName = models.CharField('本站名称', max_length=256)
    theLink = models.CharField('本站网址', max_length=256)
    theLogo = models.FileField('Logo', upload_to='./central/logo-file/')
    theQRCode = models.FileField('二维码', upload_to='./central/logo-file/')
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
class StaticAbout(models.Model):
    theName = models.CharField('链接(不要修改)', max_length=256, unique=True)
    theTitle = models.CharField('标题', max_length=256, unique=True)
    theContent = UEditorField('内容', height=300, width=1000, default=u'', blank=True, imagePath="central/content-images/", toolbars='besttome', filePath='central/content-files/')
    theImage = models.FileField('封面', upload_to='./central/about-image-files/')

    def __str__(self):
        return self.theTitle

    class Meta:
        verbose_name = '网站简介、团队成员与联系方式'
        verbose_name_plural = '关于本站'


@python_2_unicode_compatible
class HeroImages(models.Model):
    theHeroTitle = models.CharField('标题', max_length=256, unique=True)
    theImage = models.FileField('上传文件', upload_to='./central/hero-image-files/')
    theLink = models.TextField('超链接', default='')
    
    def __str__(self):
        return self.theHeroTitle

    class Meta:
        verbose_name = '轮播图片的链接和文件名'
        verbose_name_plural = '轮播图片'

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


@python_2_unicode_compatible
class Current(models.Model):
    title = models.CharField('标题', max_length=256)

    author = models.ForeignKey('auth.User', blank=True, null=True, verbose_name='作者')
    content = UEditorField('内容', height=300, width=1000, default=u'', blank=True, imagePath="branch/content-images/", toolbars='besttome', filePath='branch/content-files/')

    pub_time = models.DateTimeField('发布时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField('更新时间', auto_now=True, null=True)
    published = models.BooleanField('正式发布', default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '高校动态'
        verbose_name_plural = '发布动态'
        ordering = ['-update_time']


@python_2_unicode_compatible
class BranchList(models.Model):
    name = models.CharField('名称', max_length=256, unique=True)
    link = models.CharField('分部网址', max_length=256)
    logo = models.FileField('校徽', upload_to='./central/branchs-logo-image-files/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '高校列表'
        verbose_name_plural = '高校列表'


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    branch = models.ForeignKey(BranchList, blank=False, null=False, verbose_name='学校')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = '高校列表'
        verbose_name_plural = '高校列表'