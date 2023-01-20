from django.urls import path, include
from rest_framework import routers
from .views import LikeViewSet, RatingViewSet, CommentViewSet, ReplyViewSet, FavoriteViewSet

router = routers.DefaultRouter()
router.register('likes', LikeViewSet)
router.register('ratings', RatingViewSet)
router.register('comments', CommentViewSet)
router.register('replies', ReplyViewSet)
router.register('favorites', FavoriteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
