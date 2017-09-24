from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User, Relationship, Event, UserEvent


class RelationshipInline(admin.StackedInline):
    model = Relationship
    fk_name = 'from_user'
    extra = 0


class FeedInline(admin.StackedInline):
    model = UserEvent
    fk_name = 'user'
    extra = 0


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    inlines = [
        RelationshipInline,
        FeedInline
    ]
    exclude = ('relationships', 'feed',)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass
