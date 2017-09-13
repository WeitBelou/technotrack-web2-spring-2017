import pytest
from django.db import IntegrityError

from core.models import User
from rettiwt.models import Post


def test_post_model_save():
    """
    Tests that can save post without errors.
    """
    User(username='Name').save()

    author = User.objects.first()

    p = Post(author_id=author.id, text='Some fancy text')
    p.save()

    assert p == Post.objects.first()


def test_post_save_without_author():
    """
    Must fail when trying to save post without author.
    """
    p = Post(text='The small transformator oddly fights the star.')

    with pytest.raises(IntegrityError):
        p.save()
