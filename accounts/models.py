from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):

    USER_TYPE_CHOICES = (
        ('customer', 'Customer'),
        ('restaurant', 'Restaurant'),
    )

    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)

    def __str__(self):
        return self.username
class Address(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='addresses'
    )

    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)

    address_line = models.CharField(max_length=500)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)

    is_default = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.city}"
        from accounts.models import Address
        address = models.ForeignKey(
    Address,
    on_delete=models.SET_NULL,
    null=True,
    blank=True
)
