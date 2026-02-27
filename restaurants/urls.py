from django.urls import path
from .views import (
    RestaurantListCreateView,
    RestaurantDetailView,
    MenuItemListCreateView,
    MenuItemDetailView,
)

urlpatterns = [
    path("", RestaurantListCreateView.as_view(), name="restaurants"),
    path("<int:pk>/", RestaurantDetailView.as_view(), name="restaurant-detail"),
    path("menu/", MenuItemListCreateView.as_view(), name="menu-items"),
    path("menu/<int:pk>/", MenuItemDetailView.as_view(), name="menu-item-detail"),
]
