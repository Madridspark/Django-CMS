from django.contrib import admin
from .models import Column, Article

class ColumnAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'intro',)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'author', 'content', 'pub_time', 'update_time',)

admin.site.register(Column, ColumnAdmin)
admin.site.register(Article, ArticleAdmin)