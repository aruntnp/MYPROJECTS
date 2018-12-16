from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)


class UserManager(BaseUserManager):
    def create_user(self, email, first_name, password=None, is_admin=False, is_active=True, is_staff=False):
        if not email:
            raise ValueError("User mush have an email address!")
        if not password:
            raise ValueError("User must have password!")
        if not first_name:
            raise ValueError("User must have at-least First Name!")

        user_obj = self.model(email=self.normalize_email(email), first_name=first_name)

        user_obj.set_password(
            password)  # This is in build method so, it came here, or else user_obj.password = password
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save(using=self._db)

        return user_obj

    def create_staffuser(self, email, first_name, password=None):
        user = self.create_user(
            email,
            first_name,
            password=password,
            is_staff=True
        )

        return user

    def create_superuser(self, email, first_name, password=None):
        user = self.create_user(email, first_name, password=password, is_staff=True, is_admin=True)

        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=40, blank=True)
    last_name = models.CharField(max_length=40, blank=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    objects = UserManager()

    def __str__(self):
        return self.email

    @property
    def get_full_name(self):
        return ' '.join([self.first_name, self.last_name])

    def get_short_name(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_active(self):
        return self.active

    @property
    def is_admin(self):
        return self.admin


class GuestEmail(models.Model):
    email = models.EmailField()
    active = models.BooleanField(default=True)
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
