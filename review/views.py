<<<<<<< HEAD
from rest_framework import viewsets, permissions
from .models import Product, Like, Rating, Comment, Reply, Favorite
=======
from rest_framework import viewsets
from .models import Like, Rating, Comment, Reply, Favorite
>>>>>>> b503b9a3644e2c0641c6a15eda9afdf87ec822c4
from .serializers import LikeSerializer, RatingSerializer, CommentSerializer, ReplySerializer, FavoriteSerializer

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
<<<<<<< HEAD
    permission_classes = [permissions.IsAuthenticated]
=======
>>>>>>> b503b9a3644e2c0641c6a15eda9afdf87ec822c4

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
<<<<<<< HEAD
    permission_classes = [permissions.IsAuthenticated]
=======
>>>>>>> b503b9a3644e2c0641c6a15eda9afdf87ec822c4

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
<<<<<<< HEAD
    permission_classes = [permissions.IsAuthenticated]
=======
>>>>>>> b503b9a3644e2c0641c6a15eda9afdf87ec822c4

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ReplyViewSet(viewsets.ModelViewSet):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
