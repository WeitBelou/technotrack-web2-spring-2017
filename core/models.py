from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class WithDates(models.Model):
    created_at = models.DateTimeField('Created date.', auto_now_add=True)
    updated_at = models.DateTimeField('Last update date.', auto_now=True)

    class Meta:
        abstract = True


class WithAuthor(models.Model):
    author = models.ForeignKey(to=User)

    class Meta:
        abstract = True


class WithDatesAndAuthor(WithDates, WithAuthor):
    class Meta:
        abstract = True
