from django.urls import path,include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter

from .views import *


router = DefaultRouter()
router.register('users', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('register/', RegisterAPIView.as_view()),
    path('delete/<str:email>/', delete),
    path('logout/', LogoutView.as_view()),
    path('activate/<str:activation_code>/', activate_view),
    path('login/', LoginSerializer.as_view()),
    path('change_password/', ChangePasswordView.as_view()),
    path('forgot_password/', ForgotPasswordView.as_view()),
    path('password_confirm/<str:activation_code>/', NewPasswordView.as_view()),
]