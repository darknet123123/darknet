from rest_framework import serializers

from rest_framework_simplejwt.views import TokenObtainPairView
from .models import User
from .tasks import password_confirm

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




class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # representation['comment'] = CommentSerializer(instance.comment.all(), 
        #     many=True, context=self.context).data
        # representation['favorite'] = FavoriteSerializer(instance.favorite.all(), 
        #     many=True, context=self.context).data
        # representation['like'] = instance.like.count()
        # representation['rating'] = instance.average_rating

        return representation




class LoginSerializer(TokenObtainPairView):

    pass


class ForgotSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate(self, attrs):
        email = attrs.get('email')
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError('Such email does not found')
        return attrs
    
    def save(self):
        data = self.validated_data
        user = User.objects.get(**data)
        user.set_activation_code()
        password_confirm.delay(user.email, user.activation_code)
        

class ChangePasswordSerializer(serializers.Serializer):
   
    model = User

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(
        required=True, min_length=8, write_only=True
    )