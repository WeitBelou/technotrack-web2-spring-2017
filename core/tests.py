import pytest

from core.models import WithDates, User, WithAuthor


def test_with_dates():
    """
    Tests that we can't save WithDates model.
    """
    w = WithDates()

    with pytest.raises(AttributeError):
        w.save()


def test_with_author():
    """
    Tests that we can't save WithAuthor model
    """
    w = WithAuthor()

    with pytest.raises(AttributeError):
        w.save()


def test_user_model_save():
    """
    Tests that we can save user model.
    """
    u = User()
    u.save()

    assert u == User.objects.first()
