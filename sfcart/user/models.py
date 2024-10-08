from django.db import models
from django.contrib.auth.models import User

# for saving additional details of the user

class UserDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_details')
    profile_photo = models.ImageField(upload_to='user_profile_pictures/', blank=True, null=True)
    gender = models.CharField(max_length=6, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], blank=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    # address 
    street_address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    

    def __str__(self):
        return f"{self.user.username}'s details"