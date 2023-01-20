from rest_framework import serializers
from .models import Like, Rating, Comment, Reply, Favorite

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('id', 'user', 'product')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user_username'] = instance.user.username
        representation['product_name'] = instance.product.name
        return representation

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'user', 'product', 'rating')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user_username'] = instance.user.username
        representation['product_name'] = instance.product.name
        return representation

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'user', 'product', 'text')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user_username'] = instance.user.username
        representation['product_name'] = instance.product.name
        return representation

class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ('id', 'user', 'comment', 'text')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user_username'] = instance.user.username
        representation['comment_text'] = instance.comment.text
        return representation

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ('id', 'user', 'product')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user_username'] = instance.user.username
        representation['product_name'] = instance.product.name
        return representation
