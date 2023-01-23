from django.urls import path


from auction import views
from .views import *
urlpatterns=[
    path('categories/', views.CategoryListView.as_view(), name='categories-list'),
    path('auction/', views.AuctionListView.as_view()),

    path('get/<int:pk>', views.AuctionUserView.as_view(), name='maria'),

    path('auction/', views.AuctionListView.as_view(), name='post-list'),
    # # path('posts/', views.PostView.as_view(), name='post-list'),
    path('auction/<int:pk>/', views.AuctionDetailView.as_view(), name='product-detail'),
    




    # path('auction-detail/<int:pk>/', views.AuctionImageView.as_view()),
    path('bid-create/', views.BidCreateView.as_view()),
    # path('bid-detail/<int:pk>', views.BidDetailView.as_view()),
    path('bid/', views.BidsView.as_view()),

    # path("createbid/", views.BidCreateView.as_view()),
    path("detailbid/<int:user>", views.BidDetailView.as_view()),
    # path("bids", views.BidListView.as_view()),
    path("topbid/<int:user>/<int:auction>", views.BidTopView.as_view()),
    path("deletebid/<int:user>/<int:auction>",views.BidDeleteView.as_view())


]