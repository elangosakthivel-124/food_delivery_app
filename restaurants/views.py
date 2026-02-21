from rest_framework import generics
from .models import Restaurant, FoodItem
from .serializers import RestaurantSerializer, FoodItemSerializer


class RestaurantListAPIView(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class RestaurantDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class FoodItemListAPIView(generics.ListCreateAPIView):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer


class FoodItemDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied


class RestaurantListAPIView(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):

        user = self.request.user

        if user.user_type != 'restaurant':
            raise PermissionDenied("Only restaurant owners can create restaurants")

        serializer.save(owner=user)
