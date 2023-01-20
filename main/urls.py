from django.urls import path


from main import views
from .views import *

# # urlpatterns = [
# #     path('likefilms/', CreateLikeAPIView.as_view()),
    
# ]
urlpatterns=[
    path('categories/', views.CategoryListView.as_view(), name='categories-list'),
    # path('product/', views.ProductListView.as_view(), name='product-list'),
    # path('categories/', views.categories, name='categories-list'),

    
    path('product/', views.ProductListView.as_view(), name='post-list'),
    path('product/', views.ProductView.as_view(), name='post-list'),
    # path('product-create/', views.ProductCreateView.as_view(), name='product-create'),
    # path('product/<int:pk>/', views.ProductdetailView.as_view(), name='product-detail'),
    # path('product-update/<int:pk>/', views.ProductUpdateView.as_view()),
    # path('product-delete/<int:pk>/', views.ProductDeleteView.as_view()),
    path('product/<int:pk>/', views.ProductDetailView.as_view()),
]
