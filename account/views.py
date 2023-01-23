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
from decouple import config


from .models import User, Code, CodeLink
from .serializers import *
from .permissions import IsAdminOrAuthor
from .tasks import update_balance, password_recovery


from rest_framework.generics import get_object_or_404, UpdateAPIView
# codes = [Code(code=get_random_string(10,'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890')) for i in range(100)]


# Получение кода
@api_view(['POST'])
def get_code(request):
    if not request.user.is_authenticated:
        return Response('You have to be authenticated!', status=403) 
    code = get_random_string(10,'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890')
    coder = Code.objects.create(code=code)
    codes = Code.objects.first()
    return Response(f'Code : {codes.code}', status=201)


# проверка кода (тг бот)
@api_view(['POST'])
def check_code(request):
    code = request.data.get('code')
    print(code)
    bot_code = request.data.get('bot_code')
    if bot_code != config('TOKEN'):
        return Response('Access denied!', status=405)
    code = Code.objects.filter(code=code)
    if code.exists():
        code.delete()
        return Response('Yep', status=200)
    
# получение кода регистрации (бот)
@api_view(['GET'])
def get_code_link(request):
    code = CodeLink.objects.first()
    print(code)
    return Response(code.code, status=200)



# Регистрация аккаунта 
class RegisterAPIView(APIView):
    @swagger_auto_schema(request_body=RegisterSerializer())
    def post(self, request, code):
        code = get_object_or_404(CodeLink, code=code)
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        code.delete()
        return Response('To complete registration, follow the link sent', status=201)
        
# активация кода
@api_view(['GET'])
def activate_view(request, activation_code):
    user = get_object_or_404(User, activation_code=activation_code)
    user.is_active = True # activate user
    user.activation_code = '' # delete the activated code
    user.save()
    return Response('Succesfuly activated the account', 200)






# управление юзерами (Admin)
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser,]
    
    def get_serializer_context(self):
        return {'request':self.request}






# управление аккаунтом (User)
class UserAPIView(APIView):
    permission_classes = [IsAuthenticated,]
    
    def get(self, request):
        user = request.user
        if not user.is_authenticated:
          return Response('You are not authenticated', status=401)   
        ser = GetSerializer(user)
        return Response(ser.data, status=201)
    
    def patch(self, request):
        user = request.user
        if not user.is_authenticated:
            return Response('You are not authenticated', status=401)   
        ser = PatchSerializer(user, data=request.data, partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=204)

    def delete(self, request):
        user = request.user
        if not user.is_authenticated:
          return Response('You are not authenticated', status=401)   
        user.delete()
        return Response('Succesfully deleted!', status=205)
    







# запрос на сброс пароля
@api_view(['POST'])
def password_recover(request):
    user = request.user
    if not user.is_authenticated:
        return Response('You are not authenticated', status=401)
    user.activation_code = get_random_string(8, '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')
    user.save()
    new_password = get_random_string(8, '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')
    password_recovery.delay(user.email, user.activation_code, new_password)
    return Response('Message has been sent!', status=201)

# подтверждение сброса пароля
@api_view(['GET'])
def password_confirm(request, activation_code, new_password):
    user = get_object_or_404(User, activation_code=activation_code)
    user.set_password(new_password)
    user.save(update_fields=['password'])
    user.activation_code = ''
    user.save()
    return Response('Password has been changed!', status=201)







# пополнить баланс
@api_view(['POST'])
def balance_update(request):
    if not request.user.is_authenticated:
        return Response(status=401)
    if not request.data.get('amount'):
        return Response('amount is required', status=400)
    amount = request.data.get('amount')
    mon = format(int(amount), "b")
    result = f'{config("BALANCE_CODE")}{mon}'
    user = request.user
    user.activation_code = get_random_string(8, '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')
    user.save()
    update_balance.delay(user.email, user.balance, result, user.activation_code)
    return Response('Payment confirmation have been sent to your email', status=201)
    
# подтверждение пополнения
@api_view(['GET'])
def payment_confirm(request, activation_code, amount):
    user = get_object_or_404(User, activation_code=activation_code)
    user.balance += amount
    user.activation_code = ''
    user.save()
    return Response('Payment confirmed!', status=201)







# выход из аккаунта (обнуление токена)
class LogoutView(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        print(request.data)
        user = request.user
        Token.objects.filter(user=user).delete()
        return Response('Succesfully logged out', status=201)







# выход из аккаунта
class LogoutView(APIView):
    permission_classes=[IsAuthenticated, ]
    
    def post(self, request):
        user=request.user
        Token.objects.filter(user=user).delete()
        return Response('Successfully logged out', status=status.HTTP_200_OK)




# смена пароля
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



