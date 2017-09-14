from django.db import models

from core.models import WithDates, WithAuthor, WithDatesAndAuthor, WithGenericKey


class Likable(models.Model):
    """
    Helper to represent objects on which we can set like.
    """
    likes_count = models.PositiveIntegerField(default=0)

    class Meta:
        abstract = True


class Commentable(models.Model):
    """
    Helper to represent objects which you can comment
    """
    comments_count = models.PositiveIntegerField(default=0)

    class Meta:
        abstract = True


class Like(WithDatesAndAuthor, WithGenericKey):
    """
    Model for 'likes'.
    """

    def __str__(self):
        return 'Author {}, to {} "{}"'.format(self.author, self.content_type, self.object)


class Comment(WithDatesAndAuthor, WithGenericKey, Likable, Commentable):
    """
    Model for 'comments'
    """
    text = models.TextField(max_length=300)

    def __str__(self):
        return 'Author {}, to {} "{}"'.format(self.author, self.content_type, self.object)


class Post(WithDatesAndAuthor, Likable, Commentable):
    """
    Model for 'posts'.
    """
    text = models.TextField(max_length=300)

    @property
    def short_text(self):
        n = min(50, len(self.text) - 1)
        return self.text[:n]

    def __str__(self):
        return 'Author {}, {}'.format(self.author, self.short_text)
