from django.db.models.signals import post_save
from django.contrib.auth.models import User  # sender sending the signals
from django.dispatch import receiver    # a function get the signals and perform some task
from .models import Profile

# when a user is saved send then send the signals, signals is received by the receiver
# create_profile takes all the necessary arguments that post_save pass to it


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    # save the profile when the user is save
    instance.profile.save()
