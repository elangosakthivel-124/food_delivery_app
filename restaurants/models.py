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
        class Category(models.Model):

    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name='categories'
    )

    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.restaurant.name} - {self.name}"
class FoodItem(models.Model):

    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name='food_items'
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    name = models.CharField(max_length=255)
    description = models.TextField()

    price = models.DecimalField(max_digits=8, decimal_places=2)

    image = models.ImageField(upload_to='food_items/')

    is_available = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

