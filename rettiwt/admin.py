from django.contrib import admin
from django.contrib.admin import ModelAdmin

from rettiwt.models import Post, Like, Comment


@admin.register(Post)
class AdminPost(ModelAdmin):
    readonly_fields = ('comments_count', 'likes_count',)


@admin.register(Comment)
class AdminComment(ModelAdmin):
    readonly_fields = ('likes_count', )


@admin.register(Like)
class AdminLike(ModelAdmin):
    pass
