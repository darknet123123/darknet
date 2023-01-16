
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.crypto import get_random_string


from .tasks import send_activation_code

# Create your models here.

class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self,email,password,**kwargs):
        assert email, 'Email is required'
        email = self.normalize_email(email)
        user:User = self.model(email=email,**kwargs)
        user.set_password(password)
        user.create_activation_code()
        user.save(using=self.db)
        send_activation_code.delay(user.email,user.activation_code)
        return user

    def create_superuser(self,email,password,**kwargs):
        assert email , 'Email is required'
        kwargs['is_active'] = True
        kwargs['is_superuser']= True
        kwargs['is_staff']= True
        email = self.normalize_email(email)
        user:User = self.model(email=email,**kwargs)
        user.set_password(password)
        user.save(using=self.db)
        return user



class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50)
    avatar = models.ImageField(null=True)
    is_active = models.BooleanField(default= False)
    activation_code = models.CharField(max_length=8, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =   []

    objects = UserManager()


    @staticmethod
    def generate_activation_code():
        from django.utils.crypto import get_random_string
        code = get_random_string(8)
        return code 

    def set_activation_code(self):
        code = self.generate_activation_code()
        if User.objects.filter(activation_code=code).exists():
            self.set_activation_code()
        else:
            self.activation_code = code
            self.save()

    @property
    def average_rating(self):
        ratings = self.ratings.all()
        values = []
        for rating in ratings:
            values.append(rating.value)
        if values:
            return sum(values) / len(values)
        return 0


    def password_confirm(self):
        from django.core.mail import send_mail
        # activation_url = f'http://127.0.0.1:8000/user_account/password_confirm/{self.activation_code}'
        activation_url = f'https://tektonik.herokuapp.com/user_account/password_confirm/{self.activation_code}'
        message = f"""
        Do you want to change password?
        Confirm password changes: {activation_url}
        """
        send_mail("Please confirm your new changes", message, "apple_store@gmail.com", [self.email, ])


    def __str__(self) -> str:
        return f'{self.username} -> {self.email}'
