import pytest

from core.models import WithDates, User


def test_with_dates():
    """
    Tests that we can't save with dates.
    """
    w = WithDates()

    with pytest.raises(AttributeError):
        w.save()


def test_user_model_save():
    """
    Tests that we can save user model.
    """
    w = User()
    w.save()
