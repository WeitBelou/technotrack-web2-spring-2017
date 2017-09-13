from django.db.models.signals import post_save
from django.dispatch import receiver

from rettiwt.models import Like


@receiver(post_save, sender=Like)
def increment_likes_count(instance: Like, created=False, *args, **kwargs):
    """
    Signal that increments likes_count on associated object.
    """
    if created:
        likable = instance.object
        likable.likes_count += 1
        likable.save()
