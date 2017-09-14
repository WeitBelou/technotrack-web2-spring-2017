from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from core.models import WithDates, WithAuthor, WithDatesAndAuthor


class Like(WithDatesAndAuthor):
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


class Comment(WithDatesAndAuthor, Likable):
    """
    Model for 'comments'
    """
    text = models.TextField(max_length=300)

    object_id = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType)

    object = GenericForeignKey()


class Commentable(models.Model):
    """
    Helper to represent objects which you can comment
    """
    comments_count = models.PositiveIntegerField(default=0)

    class Meta:
        abstract = True


class Post(WithDatesAndAuthor, Likable, Commentable):
    """
    Model for 'posts'.
    """
    text = models.TextField(max_length=300)
