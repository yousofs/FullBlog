from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserProfileManager


class UserProfile(AbstractBaseUser):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    bio = models.TextField(null=True, blank=True)
    phone_number = models.PositiveBigIntegerField(null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
