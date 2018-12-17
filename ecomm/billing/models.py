from django.conf import settings
from django.db.models.signals import post_save
from django.db import models
from accounts.models import GuestEmail

User = settings.AUTH_USER_MODEL


# Create your models here.

# Model MANAGER:

class BillingProfileManager(models.Manager):

    def new_or_get(self, request):
        user = request.user
        guest_email_id = request.session.get('guest_email_id')
        obj = None
        created = None
        if user.is_authenticated():
            'logged IN user Checkout: Remember Payment Stuff'
            obj, created = self.model.objects.get_or_create(
                user=user,
                email=user.email)

        elif guest_email_id is not None:
            'Gues user Checkout: Auto reload payment stuff.'
            guest_email_obj = GuestEmail.objects.get(id=guest_email_id)
            obj, created = self.model.objects.get_or_create(
                email=guest_email_obj.email)
        else:
            pass
        return obj, created


class BillingProfile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True)
    email = models.EmailField(unique=True)
    active = models.BooleanField(default=True)
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    # active = models.BooleanField(default=True)
    # Customer_id in Stripe

    objects = BillingProfileManager()

    def __str__(self):
        return self.email


# ************************ SIGNALS *********************

def user_created_reciver(sender, instance, created, *args, **kwargs):
    if created and instance.email:
        try:
            obj = BillingProfile.objects.get(user=instance, email=instance.email)
        except:
            obj = BillingProfile.objects.create(user=instance, email=instance.email)
            obj.save()

        print(obj)

    # BillingProfile.objects.get_or_created(user=instance, email=instance.email)


post_save.connect(user_created_reciver, sender=User)
