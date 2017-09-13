from django.db import models

from core.models import WithDates


class Post(WithDates):
    text = models.TextField(max_length=300)
