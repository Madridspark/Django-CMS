# -*- coding: utf-8 -*-
from django.contrib import admin
from models import StaticInfo, StaticAbout, HeroImages, Page1Video

# 设置需要编辑的栏位
class StaticInfoAdmin(admin.ModelAdmin):
    list_display = ('theName', 'theLink', 'theLogo', 'thePartners', 'theTEL', 'theEmail', 'theAddress', 'thePostcode',)

class StaticAboutAdmin(admin.ModelAdmin):
    list_display = ('theTitle', 'theContent', 'theImage',)

class HeroImagesAdmin(admin.ModelAdmin):
    list_display = ('theHeroTitle', 'theLink', 'theImage',)

class Page1VideoAdmin(admin.ModelAdmin):
    list_display = ('theTitle', 'OGG', 'MP4', 'WEBM', 'SWF',)

# 注册管理页面
admin.site.register(StaticInfo, StaticInfoAdmin)
admin.site.register(StaticAbout, StaticAboutAdmin)
admin.site.register(HeroImages, HeroImagesAdmin)
admin.site.register(Page1Video, Page1VideoAdmin)