from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from localflavor.tn.forms import GOVERNORATE_CHOICES  # Update this import path as necessary


from .utils import user_directory_path
class Location(models.Model):
    address_1 = models.CharField(max_length=128, blank=True)
    address_2 = models.CharField(max_length=128, blank=True)
    city = models.CharField(max_length=84)
    state = models.CharField(max_length=20, choices=GOVERNORATE_CHOICES, default='sfax')
    
    def __str__(self):
        return f'{self.city}, {self.state}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=user_directory_path, null=True)
    bio = models.CharField(max_length=140, blank=True)
    phone_number = models.CharField(max_length=12, blank=True)
    location = models.OneToOneField(
        Location, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return f'{self.user.username}\'s Profile'
