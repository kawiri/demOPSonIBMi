from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    """Profile model."""
    MALE='M'
    FEMALE='F'
    OTHER='O'
    sex_choice = [(MALE, 'Male'),(FEMALE, 'Female'),(OTHER,'Other')]

    user = models.OneToOneField(User, on_delete=models.RESTRICT)
    website = models.URLField(max_length=200, blank=True)
    biography = models.TextField(blank=True)
    phone_number = models.CharField(max_length=10, blank=True)
    address = models.CharField(blank=True, max_length=80)
    city = models.CharField(blank=True, max_length=80)
    country = models.CharField(blank=True, max_length=80)
    sex = models.CharField(blank=False, max_length=1, default='O', choices=sex_choice)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    #borrar = models.CharField(max_length=30, blank=True)
    photo = models.ImageField(upload_to='users/picture', max_length=500, null=True)


    def __str__(self):
        """Return username"""
        return self.user.username
