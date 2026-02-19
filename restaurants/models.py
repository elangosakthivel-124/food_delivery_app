from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Restaurant(models.Model):

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'user_type': 'restaurant'}
    )

    name = models.CharField(max_length=255)
    description = models.TextField()
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=20)

    image = models.ImageField(upload_to='restaurants/')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
