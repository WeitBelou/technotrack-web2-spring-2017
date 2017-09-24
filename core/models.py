from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title


class User(AbstractUser):
    relationships = models.ManyToManyField(to='self', through='Relationship',
                                           symmetrical=False, related_name='related_to')
    feed = models.ManyToManyField(to=Event, through='UserEvent', related_name='users')

    def __str__(self):
        return self.username


class Relationship(models.Model):
    from_user = models.ForeignKey(User, related_name='from_users')
    to_user = models.ForeignKey(User, related_name='to_users')


class UserEvent(models.Model):
    user = models.ForeignKey(User, related_name='user')
    event = models.ForeignKey(Event, related_name='event')


class WithDates(models.Model):
    """
    Helper that provides useful dates
    """
    created_at = models.DateTimeField('Created date.', auto_now_add=True)
    updated_at = models.DateTimeField('Last update date.', auto_now=True)

    class Meta:
        abstract = True


class WithAuthor(models.Model):
    """
    Helper that provides author.
    """
    author = models.ForeignKey(to=User)

    class Meta:
        abstract = True


class WithDatesAndAuthor(WithDates, WithAuthor):
    class Meta:
        abstract = True


class WithGenericKey(models.Model):
    """
    Helper that provides GenericForeignKey related fields.
    """
    object_id = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType)

    object = GenericForeignKey()

    class Meta:
        abstract = True
