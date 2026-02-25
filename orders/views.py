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
        class PlaceOrderAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        cart = Cart.objects.get(user=request.user)
        items = cart.items.all()

        total_price = 0

        order = Order.objects.create(
            user=request.user,
            total_price=0
        )

        for item in items:
            price = item.food_item.price * item.quantity
            total_price += price

            OrderItem.objects.create(
                order=order,
                food_item=item.food_item,
                quantity=item.quantity,
                price=price
            )

        order.total_price = total_price
        order.save()

        items.delete()

        return Response({
            "message": "Order placed successfully",
            "order_id": order.id
        })
class UserOrdersAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        orders = Order.objects.filter(user=request.user)

        data = []

        for order in orders:
            data.append({
                "order_id": order.id,
                "total": order.total_price,
                "status": order.status
            })

        return Response(data)
        class PlaceOrderAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        payment_method = request.data.get('payment_method', 'cod')

        cart = Cart.objects.get(user=request.user)
        items = cart.items.all()

        total_price = 0

        order = Order.objects.create(
            user=request.user,
            total_price=0,
            payment_method=payment_method
        )

        for item in items:
            price = item.food_item.price * item.quantity
            total_price += price

            OrderItem.objects.create(
                order=order,
                food_item=item.food_item,
                quantity=item.quantity,
                price=price
            )

        order.total_price = total_price
        order.save()

        items.delete()

        return Response({
            "message": "Order placed successfully",
            "order_id": order.id,
            "payment_method": payment_method
        })
from restaurants.models import Restaurant
from rest_framework.exceptions import PermissionDenied

class RestaurantOrdersAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        if request.user.user_type != 'restaurant':
            raise PermissionDenied("Only restaurant owners allowed")

        restaurant = Restaurant.objects.filter(owner=request.user).first()

        orders = OrderItem.objects.filter(
            food_item__restaurant=restaurant
        )

        data = []

        for item in orders:
            data.append({
                "order_id": item.order.id,
                "food": item.food_item.name,
                "quantity": item.quantity,
                "status": item.order.status
            })

        return Response(data)
from django.db.models import Sum
from restaurants.models import FoodItem
