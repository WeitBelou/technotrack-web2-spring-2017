from typing import List

from django.db import models

from core.models import WithDates, WithAuthor, WithDatesAndAuthor, WithGenericKey, User


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


class FeedEvent(WithDatesAndAuthor):
    """
    Helper to represent model that adds event to associated users feeds.
    """

    def get_title(self) -> str:
        """
        Short title that will be shown in feed description.
        """
        raise NotImplementedError('You should override "get_title" method in derived classes')

    class Meta:
        abstract = True


class Like(WithGenericKey, FeedEvent):
    """
    Model for 'likes'.
    """

    def get_title(self) -> str:
        return '{author} liked {type_} {object_}'.format(
            author=self.author,
            type_=self.content_type,
            object_=self.object
        )

    def __str__(self):
        return 'Author {}, to {} "{}"'.format(self.author, self.content_type, self.object)


class Comment(WithGenericKey, FeedEvent, Likable, Commentable):
    """
    Model for 'comments'
    """
    text = models.TextField(max_length=300)

    def get_title(self) -> str:
        return '{author} commented {type_} {object_}'.format(
            author=self.author,
            type_=self.content_type,
            object_=self.object
        )

    def __str__(self):
        return 'Author {}, to {} "{}"'.format(self.author, self.content_type, self.object)


class Post(FeedEvent, Likable, Commentable):
    """
    Model for 'posts'.
    """
    text = models.TextField(max_length=300)

    @property
    def short_text(self):
        n = min(50, len(self.text) - 1)
        return self.text[:n]

    def get_title(self) -> str:
        return '{author} publish post {short}'.format(
            author=self.author,
            short=self.short_text
        )

    def __str__(self):
        return 'Author {}, {}'.format(self.author, self.short_text)
