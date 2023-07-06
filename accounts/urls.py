from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views


urlpatterns = [
    path('auth/login/', TokenObtainPairView.as_view(), name='login_view'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh_view'),

    path('auth/register/', views.RegisterAPIView.as_view()),
    path('auth/user/<int:pk>', views.CustomUserDetailAPIView.as_view()),
]
