from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('restaurants.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.urls import path
from .views import (
    RestaurantListAPIView,
    RestaurantDetailAPIView,
    FoodItemListAPIView,
    FoodItemDetailAPIView,
    CategoryListAPIView
)

urlpatterns = [
    path('restaurants/', RestaurantListAPIView.as_view()),
    path('restaurants/<int:pk>/', RestaurantDetailAPIView.as_view()),

    path('foods/', FoodItemListAPIView.as_view()),
    path('foods/<int:pk>/', FoodItemDetailAPIView.as_view()),

    path('categories/', CategoryListAPIView.as_view()),
]
from .views import (
    RestaurantListAPIView,
    RestaurantDetailAPIView,
    FoodItemListAPIView,
    FoodItemDetailAPIView,
    CategoryListAPIView,
    CreateReviewAPIView,
    TopRestaurantsAPIView
)

urlpatterns = [
    path('restaurants/', RestaurantListAPIView.as_view()),
    path('restaurants/<int:pk>/', RestaurantDetailAPIView.as_view()),

    path('foods/', FoodItemListAPIView.as_view()),
    path('foods/<int:pk>/', FoodItemDetailAPIView.as_view()),

    path('categories/', CategoryListAPIView.as_view()),

    path('review/', CreateReviewAPIView.as_view()),
    path('top-restaurants/', TopRestaurantsAPIView.as_view()),
]
