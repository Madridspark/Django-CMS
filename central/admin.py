# -*- coding: utf-8 -*-
from django.contrib import admin
from models import StaticInfo, StaticAbout, HeroImages, Page1Video, BranchList

# 设置需要编辑的栏位
class StaticInfoAdmin(admin.ModelAdmin):
    list_display = ('theName',)
    fields = ('theName', 'theLink', 'theLogo', 'thePartners', 'theTEL', 'theEmail', 'theAddress', 'thePostcode',)

class StaticAboutAdmin(admin.ModelAdmin):
    list_display = ('theTitle',)

class HeroImagesAdmin(admin.ModelAdmin):
    list_display = ('theHeroTitle',)

class Page1VideoAdmin(admin.ModelAdmin):
    list_display = ('theTitle',)

class BranchListAdmin(admin.ModelAdmin):
    list_display = ('name', 'link',)


# 注册管理页面
admin.site.register(StaticInfo, StaticInfoAdmin)
admin.site.register(StaticAbout, StaticAboutAdmin)
admin.site.register(HeroImages, HeroImagesAdmin)
admin.site.register(Page1Video, Page1VideoAdmin)
admin.site.register(BranchList, BranchListAdmin)