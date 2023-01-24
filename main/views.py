from django.shortcuts import render
# from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view, action
from .models import *
from rest_framework.response import Response
from .serializers import *
from rest_framework.views import APIView
from django.db.models import Q
from .models import *
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import generics , viewsets, status
from rest_framework import generics
from drf_yasg.utils import swagger_auto_schema




from django.utils import timezone
from datetime import timedelta
  




class CategoryListView(generics.ListAPIView):#setting urls
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    permission_classes=[AllowAny, ]
    # pagination_class = MyPaginationClass


class ProductListView(generics.ListAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    permission_classes=[AllowAny, ]


class ProductView(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    permission_classes=[AllowAny, ]

# class ProductCreateView(generics.CreateAPIView):
#     queryset=Product.objects.all()
#     serializer_class=ProductSerializer
#     # permission_classes=[IsAuthenticated, ]

class ProductDetailView(generics.RetrieveAPIView):#detail
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    permission_classes=[AllowAny, ]


# class ProductdetailView(generics.RetrieveUpdateAPIView):#detail
#     queryset=Product.objects.all()
#     serializer_class=ProductSerializer

# class ProductUpdateView(generics.UpdateAPIView):#put, patch
#     queryset=Product.objects.all()
#     serializer_class=ProductSerializer

# class ProductDeleteView(generics.DestroyAPIView):#delete
#     queryset=Product.objects.all()
#     serializer_class=ProductSerializer

from rest_framework.pagination import PageNumberPagination

class MyPaginationClass(PageNumberPagination):
    page_size=5
    def get_paginated_response(self, data):
        print(data)
        return super().get_paginated_response(data)


class ProductViewSet(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    permission_classes=[IsAuthenticated, ]
    pagination_class=MyPaginationClass

    def get_serializer_context(self):
        return {'request':self.request}

    def get_permissions(self):
        print(self.action)
        if self.action in ['update', 'partial_update', 'destroy']:#put, patch. delete
            permissions = [IsProductAuthor, ]
        else:
            permissions = [IsAuthenticated, ]
        return [permission() for permission in permissions]



    def get_queryset(self):
        queryset=super().get_queryset()
        weeks_count=int(self.request.query_params.get('days', 0))#query-params return dict
        if weeks_count>0:
            start_data=timezone.now()-timedelta(days=weeks_count)
            queryset=queryset.filter(created_at__gte=start_data)#фильтрация по  полю created_at
        return queryset

    
    @action(detail=False, methods=['get'])
    def own(self, request, pk=None):
        queryset = self.get_queryset()
        queryset = queryset.filter(seller=request.user)
        serializers =ProductSerializer(queryset, many=True,
                                       context={'request': request})
        return Response(serializers.data, status=status.HTTP_200_OK)


    @action(detail=False, methods=['get'])
    def search(self, request, pk=None):
        print(request.query_params)
        q=request.query_params.get('q')
        queryset=self.get_queryset()
        queryset=queryset.filter(Q(title__icontains=q) |
                                Q(description__icontains=q))
        serializer=ProductSerializer(queryset, many=True, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductImageView(generics.ListCreateAPIView):
    queryset=ProductImage.objects.all()
    serializer_class=ProductImageSerializer

    def get_serializer_context(self):
        return {'request':self.request}
