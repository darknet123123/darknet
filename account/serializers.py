from rest_framework import serializers
from django.core.mail import send_mail
from rest_framework_simplejwt.views import TokenObtainPairView

from config.settings import EMAIL_HOST_USER
from .models import User, Code

class RegisterSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(min_length=4,required = True)
    
    class Meta:
        model = User
        fields = ('email','password','password_confirm')

    def validate(self, attrs):
        p1 = attrs.get('password')
        p2 = attrs.pop('password_confirm')
        if p1 != p2:
            raise serializers.ValidationError("Passwords don't match")
        return attrs

    def validate_email(self,email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("User with this email already existed")
        return email

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)




class LittleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['email', 'username', 'avatar', 'balance', 'country', 'data_joined']
        


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'avatar', 'country', 'balance', 'is_active', 'is_superuser', 'date_joined']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # representation['comment'] = CommentSerializer(instance.comment.all(), 
        #     many=True, context=self.context).data
        # representation['favorite'] = FavoriteSerializer(instance.favorite.all(), 
        #     many=True, context=self.context).data
        # representation['like'] = instance.like.count()
        # representation['rating'] = instance.average_rating

        return representation


class CodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Code
        fields = '__all__'

    



class LoginSerializer(TokenObtainPairView):

    pass



class ChangePasswordSerializer(serializers.Serializer):
   
    model = User

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(
        required=True, min_length=8, write_only=True
    )

