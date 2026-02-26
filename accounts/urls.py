from django.urls import path
from .views import RegisterAPIView, LoginAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('admin/', admin.site.urls),
    path('api/', include('restaurants.urls')),
    path('api/auth/', include('accounts.urls')),
]
from .views import (
    RegisterAPIView,
    LoginAPIView,
    CreateAddressAPIView,
    UserAddressListAPIView,
    UserProfileAPIView
)

urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),

    path('profile/', UserProfileAPIView.as_view()),
    path('address/add/', CreateAddressAPIView.as_view()),
    path('addresses/', UserAddressListAPIView.as_view()),
]
from .views import OrderDetailAPIView
path('order/<int:order_id>/', OrderDetailAPIView.as_view()),
