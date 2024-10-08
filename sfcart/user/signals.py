from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserDetail

@receiver(post_save, sender=User)
def create_or_save_user_details(sender, instance, created, **kwargs):
    if created:
        UserDetail.objects.create(user=instance)
    else:
        instance.user_details.save()