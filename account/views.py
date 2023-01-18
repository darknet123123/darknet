import json
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.shortcuts import render, get_object_or_404
from rest_framework.permissions import IsAdminUser
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.authtoken.views import  ObtainAuthToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view
from django.shortcuts import redirect
from drf_yasg.utils import swagger_auto_schema
from django.utils.crypto import get_random_string


from .models import User
from .serializers import *
from .permissions import IsAdminOrAuthor
from .tasks import update_balance


from rest_framework.generics import get_object_or_404, GenericAPIView, ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
#Todo register view



# Регистрация аккаунта 
class RegisterAPIView(APIView):
    @swagger_auto_schema(request_body=RegisterSerializer())
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('Вы успешно зарегистрировались',status=201)
        

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser,]
    

    def get_serializer_context(self):
        return {'request':self.request}



# активация аккаунта
@api_view(['GET'])
def activate_view(request, activation_code):
    user = get_object_or_404(User, activation_code=activation_code)
    user.is_active = True # activate user
    user.activation_code = '' # delete the activated code
    user.save()
    return Response('Succesfuly activated the account', 200)


# подтверждение оплаты
@api_view(['GET'])
def payment_confirm(request, activation_code, amount):
    user = get_object_or_404(User, activation_code=activation_code)
    user.balance += amount
    user.activation_code = ''
    user.save()
    return Response('Payment confirmed!')



# пополнить баланс
@api_view(['POST'])
def balance_update(request, email, amount):
    account = User.objects.filter(email=email)
    if not account:
        return Response('This user does not exist', status=405)
    user = get_object_or_404(User, email=email)
    if request.user.email != email:
        return Response('It is not your email', status=405)
    user.activation_code = get_random_string(8, '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')
    user.save()
    update_balance.delay(user.email, user.balance, amount, user.activation_code)
    return Response('Payment confirmation have been sent to your email', status=201)
    


# удаление пользователей
@api_view(['DELETE'])
def delete(request, email):
    user = get_object_or_404(User, email=email)
    if request.user.email == email:
        return Response("You can't delete yourself", status=405)
    if not request.user.is_superuser:
        return Response(status=403) # запрещаем
    user.delete()
    return Response('Account has been succesfully deleted', status=204)

# выход из аккаунта (обнуление токена)
class LogoutView(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        print(request.data)
        user = request.user
        Token.objects.filter(user=user).delete()
        return Response('Succesfully logged out', status=201)


class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

 
class LogoutView(APIView):
    permission_classes=[IsAuthenticated, ]
    
    def post(self, request):
        user=request.user
        Token.objects.filter(user=user).delete()
        return Response('Successfully logged out', status=status.HTTP_200_OK)

class ChangePasswordView(UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = [IsAdminOrAuthor, ] 


    def update(self, request, *args, **kwargs):
        object = request.user
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if not object.check_password(request.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)

            object.set_password(request.data.get("new_password"))
            object.is_active = True
            object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully'
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NewPasswordView(APIView):
    def get(self, request, activation_code):
        user = get_object_or_404(User, activation_code=activation_code)
        new_password = user.create_activation_code()
        user.set_password(new_password)
        user.save()
        return Response(f"Your new password is {new_password}")

