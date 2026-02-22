from django.db import models
from django.conf import settings
from restaurants.models import FoodItem

User = settings.AUTH_USER_MODEL


class Cart(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart - {self.user}"


class CartItem(models.Model):

    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name='items'
    )

    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.food_item.name} ({self.quantity})"
class Order(models.Model):

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('delivered', 'Delivered'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id}"
        class OrderItem(models.Model):

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items'
    )

    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField()

    price = models.DecimalField(max_digits=8, decimal_places=2)
