from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User, Relationship


class RelationshipInline(admin.StackedInline):
    model = Relationship
    fk_name = 'from_user'
    extra = 0


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    inlines = (RelationshipInline,)
