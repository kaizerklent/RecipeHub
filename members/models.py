from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserAccount(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to="profiles/", default="profiles/default.png")

    def __str__(self):
        return self.email

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="profile_pics/", default="profile_default.png")

    def __str__(self):
        return f"{self.user.username} Profile"
