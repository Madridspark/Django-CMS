# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from models import StaticInfo, StaticAbout, HeroImages, Page1Video, Current, BranchList, UserProfile

# 设置需要编辑的栏位
class StaticInfoAdmin(admin.ModelAdmin):
    list_display = ('theName',)
    fields = ('theName', 'theLink', 'theLogo', 'theQRCode', 'thePartners', 'theTEL', 'theEmail', 'theAddress', 'thePostcode',)

class StaticAboutAdmin(admin.ModelAdmin):
    list_display = ('theTitle',)

class HeroImagesAdmin(admin.ModelAdmin):
    list_display = ('theHeroTitle',)

class Page1VideoAdmin(admin.ModelAdmin):
    list_display = ('theTitle',)

class CurrentAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_time', 'update_time', 'published')
    search_fields = ('title', 'content', 'author', 'pub_time', 'update_time', 'published')
    list_filter = ('author', 'pub_time', 'update_time', 'published')

class BranchListAdmin(admin.ModelAdmin):
    list_display = ('name', 'link',)

class ProfileInline(admin.StackedInline):
    model = UserProfile
    max_num = 1
    can_delete = False

class UserProfileAdmin(UserAdmin):
    inlines = [ProfileInline, ]


# 注册管理页面
admin.site.register(StaticInfo, StaticInfoAdmin)
admin.site.register(StaticAbout, StaticAboutAdmin)
admin.site.register(HeroImages, HeroImagesAdmin)
admin.site.register(Page1Video, Page1VideoAdmin)
admin.site.register(Current, CurrentAdmin)
admin.site.register(BranchList, BranchListAdmin)
admin.site.unregister(User)
admin.site.register(User, UserProfileAdmin)