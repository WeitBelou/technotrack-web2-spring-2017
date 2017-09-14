from django.contrib import admin
from django.contrib.admin import ModelAdmin

from rettiwt.models import Post, Like, Comment


@admin.register(Post)
class AdminPost(ModelAdmin):
    pass


@admin.register(Like)
class AdminLike(ModelAdmin):
    pass


@admin.register(Comment)
class AdminComment(ModelAdmin):
    pass
