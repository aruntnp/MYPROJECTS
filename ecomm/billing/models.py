from django.conf import settings
from django.db.models.signals import post_save
from django.db import models

User = settings.AUTH_USER_MODEL


# Create your models here.

class BillingProfile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True)
    email = models.EmailField()
    active = models.BooleanField(default=True)
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    # active = models.BooleanField(default=True)
    # Customer_id in Stripe

    def __str__(self):
        return self.email


# ************************ SIGNALS *********************

def user_created_reciver(sender, instance, created, *args, **kwargs):
    if created and instance.email:
        BillingProfile.objects.get_or_created(user=instance, email=instance.email)


post_save.connect(user_created_reciver, sender=User)
