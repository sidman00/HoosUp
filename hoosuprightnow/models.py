from django.db import models
from django.utils.deconstruct import deconstructible
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import ast

# Create your models here.

@deconstructible
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    activity = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    class Meta:
        managed = True