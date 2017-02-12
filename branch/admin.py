# -*- coding: utf-8 -*-
from django.contrib import admin
from models import BranchInfo, Column, Article, FriendlyLink

# 设置需要编辑的栏位
class BranchInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'hero',)

class FriendlyLinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'image',)

class ColumnAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'titleImage', 'author', 'content', 'pub_time', 'update_time', 'published')

# 注册管理页面
admin.site.register(BranchInfo, BranchInfoAdmin)
admin.site.register(FriendlyLink, FriendlyLinkAdmin)
admin.site.register(Column, ColumnAdmin)
admin.site.register(Article, ArticleAdmin)