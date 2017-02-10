# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Column, Article

# 设置需要编辑的栏位
class ColumnAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'content', 'pub_time', 'update_time', 'published')

# 注册管理页面
admin.site.register(Column, ColumnAdmin)
admin.site.register(Article, ArticleAdmin)