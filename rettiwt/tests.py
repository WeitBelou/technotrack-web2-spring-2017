import pytest
from django.db import IntegrityError

from core.models import User
from rettiwt.models import Post, Likable, Like


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


def test_likable():
    likable = Likable()

    with pytest.raises(AttributeError):
        likable.save()


def test_post_like():
    post_author = User(username='one')
    post_author.save()

    like_author = User(username='two')
    like_author.save()

    post = Post(author_id=post_author.id)
    post.save()

    like = Like(author_id=like_author.id, object=post)
    like.save()

    assert post.likes_count == 1, 'Likes count did not change.'
