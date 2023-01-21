from rest_framework.serializers import ModelSerializer

from .models import  *

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        exclude = ('author',)

    def validate(self, attrs):
        attrs =  super().validate(attrs)
        request = self.context.get('request')
        attrs['author'] = request.user
        return attrs

    def to_representation(self, instance: Comment):
        rep = super().to_representation(instance)
        rep['author'] = instance.author.email
        rep['likes'] = instance.likes.count()
        del rep['product']
        return rep


class RatingSerializer(ModelSerializer):
    class Meta:
        model = Rating
        exclude = ('author',)
    
    def validate(self, attrs):
        attrs = super().validate(attrs)
        request = self.context.get('request')  
        attrs['author'] = request.user
        return attrs

    
class FavoriteSerializer(ModelSerializer):
    class Meta:
        model = Favourite
        exclude =('author',)

    def validate(self, attrs):
        attrs =  super().validate(attrs)
        request = self.context.get('request')
        attrs['author'] = request.user
        return attrs
        

class LikeSerialzier(ModelSerializer):
    class Meta:
        model = LikeProduct
        exclude = ('author',)

class LikeCommentSerializer(ModelSerializer):
    class Meta:
        model = LikeComment
        exclude = ('author',)




















# from rest_framework import serializers
# from .models import Like, Rating, Comment, Reply, Favorite

# class LikeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Like
#         fields = ('id', 'user', 'product')

#     def to_representation(self, instance):
#         representation = super().to_representation(instance)
#         representation['user_username'] = instance.user.username
#         representation['product_name'] = instance.product.name
#         return representation

# class RatingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Rating
#         fields = ('id', 'user', 'product', 'rating')

#     def to_representation(self, instance):
#         representation = super().to_representation(instance)
#         representation['user_username'] = instance.user.username
#         representation['product_name'] = instance.product.name
#         return representation

# class CommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = ('id', 'user', 'product', 'text')

#     def to_representation(self, instance):
#         representation = super().to_representation(instance)
#         representation['user_username'] = instance.user.username
#         representation['product_name'] = instance.product.name
#         return representation

# class ReplySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Reply
#         fields = ('id', 'user', 'comment', 'text')

#     def to_representation(self, instance):
#         representation = super().to_representation(instance)
#         representation['user_username'] = instance.user.username
#         representation['comment_text'] = instance.comment.text
#         return representation

# class FavoriteSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Favorite
#         fields = ('id', 'user', 'product')

#     def to_representation(self, instance):
#         representation = super().to_representation(instance)
#         representation['user_username'] = instance.user.username
#         representation['product_name'] = instance.product.name
#         return representation
