from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=255, blank=True)
    # profile_picture = models.ImageField(upload_to='profile_pictures', blank=True)
    website = models.URLField(max_length=255, blank=True)
    # created_at = models.DateTimeField(auto_now_add=True)


class Post(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    caption = models.CharField(max_length=255)
    # image = models.ImageField(upload_to='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

