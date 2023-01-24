from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.crypto import get_random_string


from .tasks import send_activation_code


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self,email,password,**kwargs):
        assert email, 'Email is required'
        email = self.normalize_email(email)
        user:User = self.model(email=email,**kwargs)
        user.set_password(password)
        user.create_activation_code()
        user.country.upper()
        user.save(using=self.db)
        send_activation_code.delay(user.email, user.activation_code)
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
    username = models.CharField(max_length=50, default='Anonymous User')
    avatar = models.ImageField(blank=True, upload_to='avatars/')
    is_active = models.BooleanField(default=False)
    activation_code = models.CharField(max_length=8, blank=True)
    country = models.CharField(max_length=2, default='World')
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=10)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =   []

    objects = UserManager()

    def __str__(self):
        return self.email
    
    def create_activation_code(self):
        activ_code = get_random_string(8,'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890')
        self.activation_code = activ_code
        self.save()
        return activ_code

    
    def set_activation_code(self):
        code = self.create_activation_code()
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


class Code(models.Model):
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.code

<<<<<<< HEAD
class CodeLink(models.Model):
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.code
=======
>>>>>>> 4cdce7b (bug)


# import requests
# requests.get('http://127.0.0.1:8000/account/register/')