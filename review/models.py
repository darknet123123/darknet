from django.db import models
from main.models import Product
from account.models import User


class Like(models.Model):
    user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='likes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Rating(models.Model):
    user = models.ForeignKey(User, related_name='ratings', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='retings', on_delete=models.CASCADE)
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    user = models.ForeignKey(User,related_name='comments', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Reply(models.Model):
    user = models.ForeignKey(User, related_name='repls', on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, related_name='repls', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Favorite(models.Model):
    user = models.ForeignKey(User, related_name='favorits', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='favorits', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    value = models.IntegerField(choices=[(1,1), (2,2), (3,3), (4,4), (5,5)])