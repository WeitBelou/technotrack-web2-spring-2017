from django.db import models

from core.models import WithDates, WithAuthor


class Post(WithDates, WithAuthor):
    text = models.TextField(max_length=300)
