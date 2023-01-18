from django.urls import path,include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter

from .views import *


router = DefaultRouter()
router.register('users', UserViewSet)

'''
create ---------> users/ POST
list -----------> users/ GET
retrieve -------> users/id/ GET
update ---------> users/id/ PUT
partial-update -> users/id/ PATCH
destroy --------> users/id/ DELETE
'''


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
    path('update_balance/<str:email>/<int:amount>/', balance_update),
    path('payment/<str:activation_code>/<int:amount>/', payment_confirm),
]