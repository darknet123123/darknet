from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from .serializers import RegisterSerializer
from .models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token



# Регистрация аккаунта 
class RegisterAPIView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('Вы успешно зарегистрировались',status=201)
        
# активация аккаунта
@api_view(['GET'])
def activate_view(request, activation_code):
    user = get_object_or_404(User, activation_code=activation_code)
    user.is_active = True # activate user
    user.activation_code = '' # delete the activated code
    user.save()
    return Response('Successfuly activated the account', 200)

# удаление пользователей
@api_view(['DELETE'])
def delete(request, email):
    user = get_object_or_404(User, email=email)
    if not request.user.is_superuser:
        return Response(status=403) # запрещаем
    user.delete()
    return Response('Успешно удалили акаунт', status=204)

# выход из аккаунта (обнуление токена)
class LogoutView(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        print(request.data)
        user = request.user
        Token.objects.filter(user=user).delete()
        return Response('Succesfully logged out', status=201)