from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Cart, CartItem, Order, OrderItem
from restaurants.models import FoodItem


class AddToCartAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        food_id = request.data.get('food_id')
        quantity = request.data.get('quantity', 1)

        food = FoodItem.objects.get(id=food_id)

        cart, created = Cart.objects.get_or_create(user=request.user)

        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            food_item=food
        )

        if not created:
            cart_item.quantity += int(quantity)
        else:
            cart_item.quantity = quantity

        cart_item.save()

        return Response({"message": "Item added to cart"})
