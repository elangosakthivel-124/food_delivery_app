from django.urls import path
from .views import RegisterAPIView, LoginAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('admin/', admin.site.urls),
    path('api/', include('restaurants.urls')),
    path('api/auth/', include('accounts.urls')),
]
