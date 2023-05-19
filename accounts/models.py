from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import CustomUserManager

# Create your models here.

status_list = (
    ('student', 'Talaba'),
    ('meneger', 'Menejer')
)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField("First_name", max_length=100)
    last_name = models.CharField("Last name", max_length=100)
    email = models.EmailField('Email', max_length=254, unique=True)
    status = models.CharField('Status', max_length=7,
                              choices=status_list, default='student')
    is_staff = models.BooleanField('is staff', default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(
        'Updated profile', auto_now=True, blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def full_name(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.first_name + ' ' + self.last_name
