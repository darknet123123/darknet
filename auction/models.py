from operator import mod
from django.db import models
from django.contrib.auth.models import User
# from django.core.validators import MaxValueValidator, MinValueValidator 
from account.models import User
from django.db import models
from account.models import User
from datetime import date, timedelta

class AuctionCategory(models.Model):
    slug=models.SlugField(max_length=55, primary_key=True)
    name=models.CharField(max_length=55, unique=True)

    def __str__(self):
        return self.name

class Auction(models.Model):
       auction_id=models.BigAutoField(primary_key=True)
       title= models.CharField( max_length=1000,blank=False)
       description=models.TextField()
       category=models.ForeignKey(AuctionCategory, related_name='auction', on_delete=models.CASCADE)
       start_price = models.DecimalField(max_digits=10,decimal_places=2)
       start_time = models.DateTimeField(auto_now_add=True)
       end_time = models.DateTimeField(auto_now_add=True)

        
    # def __str__(self):
    #     return self.title

class AuctionImage(models.Model):
    image = models.ImageField(upload_to='auction', blank=True, null=True)
    product = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name='images')

class Bid(models.Model):
       bid_id = models.BigAutoField(primary_key=True)
       user= models.ForeignKey(User, on_delete=models.CASCADE, related_name='auction')
       auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name='auction')
       offer=models.DecimalField(max_digits=1000,decimal_places=2)
       bid_time = models.DateField(auto_now_add = True)
       product_sold = models.BooleanField(default=False)
