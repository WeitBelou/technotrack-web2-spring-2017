from django.contrib import admin
from django.contrib.admin import ModelAdmin

from rettiwt.models import Post


@admin.register(Post)
class AdminPost(ModelAdmin):
    pass
