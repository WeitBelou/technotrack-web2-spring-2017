from django.contrib.auth.models import AbstractUser
from django.db.models import Model, DateTimeField


class WithDates(Model):
    created_at = DateTimeField('Created date.', auto_now_add=True)
    updated_at = DateTimeField('Last update date.', auto_now=True)

    class Meta:
        abstract = True


class User(AbstractUser):
    pass
