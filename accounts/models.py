from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Userprofile(models.Model):
    bio = models.CharField(max_length=100)
    user = models.OneToOneField(User, models.CASCADE)
    picture = models.ImageField(upload_to="profile_picture")
