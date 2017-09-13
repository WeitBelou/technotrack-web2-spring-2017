from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from core.models import WithDates, WithAuthor


class Like(WithDates, WithAuthor):
    """
    Model for 'likes'.
    """
    object_id = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType)

    object = GenericForeignKey()


class Likable(models.Model):
    """
    Helper to represent objects on which we can set like.
    """
    likes_count = models.PositiveIntegerField(default=0)

    class Meta:
        abstract = True


class Post(WithDates, WithAuthor, Likable):
    """
    Model for 'posts'.
    """
    text = models.TextField(max_length=300)
