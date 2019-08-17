from django.db.models.signals import post_save
from django.dispatch import receiver

from airtech.apps.authentication.models import Profile, User


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    create profile upon user registration.
    """
    if created:
        Profile.objects.create(user=instance)
        instance.profile.save()
