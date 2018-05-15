from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # avatar_thumbnail = ProcessedImageField(upload_to='avatars',processors=[ResizeToFill(100, 50)],format='JPEG', options={'quality': 60})
    avatar = models.ImageField(upload_to='avatar', blank=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateTimeField(null=True, blank=True)

class Image(models.Model):
    image = models.ImageField(upload_to='post/')
    image_name = models.CharField(max_length=30)
    image_caption = models.TextField()
    # image_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
