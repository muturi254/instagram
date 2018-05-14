from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


# Create your models here.
class Profile(models.Model):
    GENDER_CHOICE =(
        ('male', 'Male'),
        ('female', 'Female')
    )
    profile_icon = ProcessedImageField(upload_to='avatars', processors=[ResizeToFill(100, 50)],format='JPEG', options={'quality': 60})
    bio = models.TextField()
    username = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICE, default='None')

class Comments(models.Model):
    comentor = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()

class Likes(models.Model):
    user_like = models.ForeignKey(User, on_delete=models.CASCADE)
    

class Image(models.Model):
    image = models.ImageField(upload_to='uploads/')
    image_name = models.CharField(max_length=30)
    image_caption = models.TextField()
    image_likes = models.ForeignKey(Likes, on_delete=models.CASCADE)
    image_comments = models.ForeignKey(Comments, on_delete=models.CASCADE)
    image_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    upload_date = models.DateField(auto_now_add=True)

