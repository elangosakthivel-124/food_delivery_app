from django.urls import path
from .views import AddToCartAPIView, PlaceOrderAPIView, UserOrdersAPIView

urlpatterns = [
    path('cart/add/', AddToCartAPIView.as_view()),
    path('order/place/', PlaceOrderAPIView.as_view()),
    path('orders/', UserOrdersAPIView.as_view()),
]
