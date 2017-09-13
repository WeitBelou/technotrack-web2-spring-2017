from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from core.models import WithDates, WithAuthor


class Post(WithDates, WithAuthor):
    """
    Model for 'posts'.
    """
    text = models.TextField(max_length=300)


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
    likes = models.ManyToManyField(Like)
    likes_count = models.PositiveIntegerField()

    class Meta:
        abstract = True
