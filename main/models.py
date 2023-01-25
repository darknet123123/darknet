from operator import mod
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator 
from account.models import User

class Category(models.Model):
    slug = models.SlugField(max_length=255, primary_key=True)
    name= models.CharField(max_length=255, unique=True)
    

    def __str__(self):
        return self.name

class Product(models.Model):
   

    title=models.CharField(max_length=10000,blank=False)
    description=models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category=models.ForeignKey(Category, on_delete=models.CASCADE,  related_name='product')
    quantity = models.PositiveIntegerField(verbose_name='quantity')
    warning=models.TextField()
    seller=models.ForeignKey(User, on_delete=models.CASCADE, related_name='product')
    created_at=models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='product', blank=True, null=True)

    def __str__(self):
        return self.title

    # @property
    # def average_rating(self):
    #     ratings = self.ratings.all()
    #     values = []
    #     for rating in ratings :
    #         values.append(rating.value)
    #     if values:
    #         return sum(values) / len(values)
    #     return 0

    # class Meta:
    #     ordering = ['id']
    
  



    
