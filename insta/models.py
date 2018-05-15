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

    def __str__(self):
        return self.user.username

class Image(models.Model):
    image = models.ImageField(upload_to='posts/')
    image_name = models.CharField(max_length=30)
    image_caption = models.TextField(blank=True)
    image_likes = models.PositiveIntegerField(default=0)
    post_date = models.DateTimeField(auto_now_add=True)
    image_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    users_liked = models.ManyToManyField(User, related_name='post_likes')

    class Meta:
        ordering = ['-post_date']


class Comments(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Image, on_delete=models.CASCADE, null=True)
    body = models.TextField(blank=True)

    def __str__(self):
        return self.body
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
