from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")
    country = models.CharField(max_length=64)

class SharedNews(models.Model):
    user = models.ManyToManyField(User, related_name="shared_news") #won't delete if user is deleted, so do it manually
    full_name = models.CharField(max_length=64)
    caption = models.TextField(max_length=2048) #for paragraph like text

    image = models.URLField(max_length=2048)
    url = models.URLField(max_length=2048)
    author = models.CharField(max_length=64)

    title = models.TextField(max_length=512)
    description = models.TextField(max_length=512)

    source = models.CharField(max_length=64)
    category = models.CharField(max_length=64)
    published_at = models.CharField(max_length=64)
    datetime_shared = models.CharField(max_length=64)

