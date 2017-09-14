import pytest
from django.db import IntegrityError

from core.models import User
from rettiwt.models import Post, Likable, Like, Commentable, Comment


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


def test_commentable():
    commentable = Commentable()

    with pytest.raises(AttributeError):
        commentable.save()


def test_post_comment():
    post_author = User(username='one')
    post_author.save()

    comment_author = User(username='two')
    comment_author.save()

    post = Post(author_id=post_author.id, text='Sunt lunaes tractare magnum, secundus fiscinaes.')
    post.save()

    comment = Comment(author_id=comment_author.id, object=post, text='Xiphiass experimentum in cella!')
    comment.save()

    assert post.comments_count == 1, 'Comments count did not change.'
