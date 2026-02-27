from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    USER_TYPES = (
        ('customer', 'Customer'),
        ('restaurant', 'Restaurant Owner'),
    )

    user_type = models.CharField(
        max_length=20,
        choices=USER_TYPES,
        default='customer'
    )


class Address(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='addresses'
    )

    full_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    address_line = models.CharField(max_length=500)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)

    is_default = models.BooleanField(default=False)
