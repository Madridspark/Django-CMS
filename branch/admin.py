# -*- coding: utf-8 -*-
from django.contrib import admin
from models import BranchInfo, Column, Article, FriendlyLink, Tools, Advertisements, Post, PostReply

# 设置需要编辑的栏位
class BranchInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'hero',)

class FriendlyLinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'link',)

class ToolsAdmin(admin.ModelAdmin):
    list_display = ('title', 'link',)

class AdvertisementsAdmin(admin.ModelAdmin):
    list_display = ('title', 'link',)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_time', 'update_time', 'published')
    search_fields = ('title', 'content', 'author', 'pub_time', 'update_time', 'published')
    list_filter = ('column', 'author', 'pub_time', 'update_time', 'published')
    filter_horizontal = ('column',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_time')
    search_fields = ('title', 'content', 'author', 'pub_time')
    list_filter = ('author', 'pub_time')

class PostReplyAdmin(admin.ModelAdmin):
    list_display = ('author', 'pub_time', 'content', 'to')
    search_fields = ('content', 'author', 'pub_time')
    list_filter = ('author', 'pub_time', 'to')

# 注册管理页面
admin.site.register(BranchInfo, BranchInfoAdmin)
admin.site.register(FriendlyLink, FriendlyLinkAdmin)
admin.site.register(Tools, ToolsAdmin)
admin.site.register(Advertisements, AdvertisementsAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Column)
admin.site.register(Post, PostAdmin)
admin.site.register(PostReply, PostReplyAdmin)