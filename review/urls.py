from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register('comments', CommentViewSet)



urlpatterns = [
    path('',include(router.urls)),
    path('rating/', CreateRatingAPIView.as_view()),
    path('likeproduct/', CreateLikeProductAPIView.as_view()),
    path('favourite/', CreateFavouriteAPIView.as_view()),
]