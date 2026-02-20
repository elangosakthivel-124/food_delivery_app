from django.urls import path
from .views import (
    RestaurantListAPIView,
    RestaurantDetailAPIView,
    FoodItemListAPIView,
    FoodItemDetailAPIView,
)

urlpatterns = [
    path('restaurants/', RestaurantListAPIView.as_view()),
    path('restaurants/<int:pk>/', RestaurantDetailAPIView.as_view()),

    path('foods/', FoodItemListAPIView.as_view()),
    path('foods/<int:pk>/', FoodItemDetailAPIView.as_view()),
]
