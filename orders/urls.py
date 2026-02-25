from django.urls import path
from .views import AddToCartAPIView, PlaceOrderAPIView, UserOrdersAPIView

urlpatterns = [
    path('cart/add/', AddToCartAPIView.as_view()),
    path('order/place/', PlaceOrderAPIView.as_view()),
    path('orders/', UserOrdersAPIView.as_view()),
]
from .views import (
    AddToCartAPIView,
    PlaceOrderAPIView,
    UserOrdersAPIView,
    RestaurantOrdersAPIView,
    UpdateOrderStatusAPIView,
    RestaurantDashboardAPIView,
    PopularFoodsAPIView
)

urlpatterns = [
    path('cart/add/', AddToCartAPIView.as_view()),
    path('order/place/', PlaceOrderAPIView.as_view()),
    path('orders/', UserOrdersAPIView.as_view()),

    path('restaurant/orders/', RestaurantOrdersAPIView.as_view()),
    path('restaurant/dashboard/', RestaurantDashboardAPIView.as_view()),
    path('restaurant/order/<int:order_id>/update/', UpdateOrderStatusAPIView.as_view()),

    path('popular-foods/', PopularFoodsAPIView.as_view()),
]
