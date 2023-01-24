from django.urls import path,include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter

from .views import *
from .tasks import get_string_time


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
    path('', include(router.urls)), # админка по упралению юзерами (16-21 строки)

    path('token/', TokenObtainPairView.as_view()), 
    path('token/refresh/', TokenRefreshView.as_view()),
    path('logout/', LogoutView.as_view()),
    
    path('user/', UserAPIView.as_view()), # управление юзера юзером (get, patch, delete)
    
    path('get_code/', get_code), # получение кода приглашения

    path('register/<str:code>/', RegisterAPIView.as_view()), # регистрация (только через бота) (email, password, password_confirm)
    path('activate/<str:activation_code>/', activate_view), # подтверждение (ссылка)


# urls of Bot
    path('get_code_bot/', get_code_link),
    path('check_code/', check_code),
#
    

    path('update_balance/', balance_update), # пополнение баланса (amount)
    path('payment/<str:activation_code>/<int:amount>/', payment_confirm), # подтверждение оплаты (почта)
   
    path('change_password/', ChangePasswordView.as_view()), # изменение пароля (email, old_password, new_password)
    path('forgot_password/', password_recover), # сбросить пароль
    path('forgot_password_confirm/<str:activation_code>/<str:new_password>/', password_confirm) # подтверждение сброса пароля (на почту выслан новый пароль)
]
