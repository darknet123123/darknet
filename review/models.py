from django.db import models
from main.models import Product
from django.db import models
# from main.models import Priduct
from account.models import User

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


class Comment(models.Model):
    product = models.ForeignKey(Product, related_name='comments', on_delete=models.CASCADE)########################
    author = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author} : {self.body}'


class LikeComment(models.Model):
    author = models.ForeignKey(User, related_name='comment_likes', on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, related_name='likes', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.author} -> {self.comment}"

class Rating(models.Model):
    product= models.ForeignKey(Product, related_name='ratings', on_delete=models.CASCADE)############################
    author = models.ForeignKey(User, related_name='ratings', on_delete=models.CASCADE)
    value = models.IntegerField(choices=[(1,1),(2,2),(3,3),(4,4),(5,5)])

    def __str__(self):
        return f'{self.author} -> {self.product}'
    


class Favourite(models.Model):
    author = models.ForeignKey(User, related_name='favourites', on_delete=models.CASCADE)#########################33
    product = models.ForeignKey(Product, related_name='favourites', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product}'



class LikeProduct(models.Model):#
    author = models.ForeignKey(User, related_name='product_likes', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='likes',on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.author} -> {self.product}'

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Reply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    value = models.IntegerField(choices=[(1,1), (2,2), (3,3), (4,4), (5,5)])

