
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, permissions
from .models import Like, Rating, Comment, Reply, Favorite
from .serializers import LikeSerializer, RatingSerializer, CommentSerializer, ReplySerializer, FavoriteSerializer

from .models import Comment, LikeProduct, Favourite, LikeComment, Rating
from .serializers import CommentSerializer, LikeCommentSerializer, RatingSerializer, FavoriteSerializer, LikeSerialzier
from .permissions import IsAuthorOrReadOnly


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly]

    @action(['POST'], detail=False)
    def like(self,request):
        user = request.user
        ser = LikeCommentSerializer(data=request.data, context={'request':request})
        ser.is_valid(raise_exception=True)
        comment_id = request.data.get("comment")

        if LikeComment.objects.filter(author=user, comment_id=comment_id).exists():
            LikeComment.objects.filter(author=user, comment_id=comment_id).delete()
        else:
            LikeComment.objects.create(author=user, comment_id=comment_id)
        return Response(status=201)


class CreateFavouriteAPIView(APIView):
    permission_classes = [IsAuthorOrReadOnly]
    @swagger_auto_schema(request_body=FavoriteSerializer())
    def post(self, request):
        user = request.user
        ser = FavoriteSerializer(data=request.data, context={'request':request})
        ser.is_valid(raise_exception=True)
        film_id =request.data.get("product")

        if Favourite.objects.filter(product_id=film_id, author=user).exists():
            Favourite.objects.filter(product_id=film_id, author=user).delete()
        else:
            Favourite.objects.create(product_id=film_id, author=user)
        return Response(status=201)
    

class CreateLikeProductAPIView(APIView):
    permission_classes = [IsAuthorOrReadOnly]
    @swagger_auto_schema(request_body=LikeSerialzier())
    def post(self, request):
        user = request.user
        ser = LikeSerialzier(data=request.data, context={'request':request})
        ser.is_valid(raise_exception=True)
        film_id = request.data.get("product")

        if LikeProduct.objects.filter(product_id=film_id,author=user).exists():
            LikeProduct.objects.filter(product_id=film_id,author=user).delete()
        else:
            LikeProduct.objects.create(product_id=film_id,author=user)
        return Response(status=201)


class CreateRatingAPIView(APIView):
    permission_classes = [IsAuthorOrReadOnly]
    @swagger_auto_schema(request_body=RatingSerializer())
    def post(self, request):
        user = request.user
        ser = RatingSerializer(data=request.data, context={'request':request})
        ser.is_valid(raise_exception=True)
        film_id = request.data.get('product')

        if Rating.objects.filter(author=user,product_id=film_id).exists():####
            rating = Rating.objects.get(author=user, product_id=film_id)#####
            rating.value = request.data.get('value')
            rating.save()
        else:
            ser.save()
        return Response(status=201)  










































# from rest_framework import viewsets, permissions
# from .models import Product, Like, Rating, Comment, Reply, Favorite
# from .serializers import LikeSerializer, RatingSerializer, CommentSerializer, ReplySerializer, FavoriteSerializer

# class LikeViewSet(viewsets.ModelViewSet):
#     queryset = Like.objects.all()
#     serializer_class = LikeSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)

# class RatingViewSet(viewsets.ModelViewSet):
#     queryset = Rating.objects.all()
#     serializer_class = RatingSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)

# class CommentViewSet(viewsets.ModelViewSet):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)

# class ReplyViewSet(viewsets.ModelViewSet):
#     queryset = Reply.objects.all()
#     serializer_class = ReplySerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)

# class FavoriteViewSet(viewsets.ModelViewSet):
#     queryset = Favorite.objects.all()
#     serializer_class = FavoriteSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
