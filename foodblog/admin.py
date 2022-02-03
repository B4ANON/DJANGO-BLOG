from typing import List
from django.contrib import admin

# Register your models here.
from .models import Category, Posts, Comment

class TitleCategory(admin.ModelAdmin):
    list_display = ('title',)

class TitlePosts(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('cat',)


admin.site.register(Posts,TitlePosts)
admin.site.register(Category,TitleCategory)
admin.site.register(Comment)