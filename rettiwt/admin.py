from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.contenttypes.admin import GenericStackedInline

from rettiwt.models import Post, Like, Comment


class LikesInline(GenericStackedInline):
    model = Like


class CommentsInline(GenericStackedInline):
    model = Comment


@admin.register(Post)
class AdminPost(ModelAdmin):
    readonly_fields = ('comments_count', 'likes_count',)
    inlines = (LikesInline, CommentsInline,)


@admin.register(Comment)
class AdminComment(ModelAdmin):
    readonly_fields = ('comments_count', 'likes_count',)
    inlines = (LikesInline, CommentsInline,)


@admin.register(Like)
class AdminLike(ModelAdmin):
    pass
