from django.db import models

# Create your models here.
class Profile(models.Model):
    GENDER_CHOICE =(
        ('male', 'Male'),
        ('female', 'Female')
    )
    profile_icon = models.ImageField(upload_to='profile')
    bio = models.TextField()
    username = models.CharField(max_length=20)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICE, default='None')

class Comments(models.Model):
    # comentor = models.ForeignKey(User, on_delete=models.CASCADE)

    pass

class Image(models.Model):
    image = models.ImageField(upload_to='uploads/')
    image_name = models.CharField(max_length=30)
    image_caption = models.TextField()
    # image_likes = models.ForeignKey(Profile)
    image_comments = models.ForeignKey(Comments)
    # image_owner = models.ForeignKey(Profile)