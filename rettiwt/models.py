from django.db import models

from core.models import WithDates, WithAuthor, WithDatesAndAuthor, WithGenericKey


class Like(WithDatesAndAuthor, WithGenericKey):
    """
    Model for 'likes'.
    """


class Likable(models.Model):
    """
    Helper to represent objects on which we can set like.
    """
    likes_count = models.PositiveIntegerField(default=0)

    class Meta:
        abstract = True


class Comment(WithDatesAndAuthor, WithGenericKey, Likable):
    """
    Model for 'comments'
    """
    text = models.TextField(max_length=300)


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
