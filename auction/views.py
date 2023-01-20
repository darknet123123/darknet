# from django.shortcuts import render

# # Create your views here.
# from django.shortcuts import render
# from django.views import View
# from .models import *
# from .serializers import *

# from django.shortcuts import render
# # from django.contrib.auth import get_user_model
# from rest_framework.decorators import api_view, action
# from .models import *
# from rest_framework.response import Response
# from .serializers import *
# from rest_framework.views import APIView
# from django.db.models import Q
# from .models import *
# from .permissions import *
# from rest_framework import generics , viewsets, status
# from rest_framework.permissions import AllowAny, IsAuthenticated

# from django.utils import timezone
# from datetime import timedelta

# from django.utils import timezone 
# import datetime   
# from datetime import date, timedelta  
# from rest_framework.views import APIView
  
# class CategoryListView(generics.ListAPIView):#setting urls
#     queryset=AuctionCategory.objects.all()
#     serializer_class=CategorySerializer
#     permission_classes=[AllowAny, ]
#     # pagination_class = MyPaginationClass

# class AuctionDetailView(generics.RetrieveUpdateAPIView):#detail
#     queryset=Auction.objects.all()
#     serializer_class=AuctionSerializer
#     permission_classes=[AllowAny, ]


# class AuctionListView(generics.ListAPIView):
#     queryset=Auction.objects.all()
#     serializer_class=AuctionSerializer
#     permission_classes=[AllowAny, ]

# class AuctionViewSet(viewsets.ModelViewSet):
#     queryset=Auction.objects.all()
#     serializer_class=AuctionSerializer
#     permission_classes=[IsAuthenticated, ]
#     # pagination_class=MyPaginationClass

# #TODO delete update author не работают

#     def get_permissions(self):
#         print(self.action)
#         if self.action in ['update', 'partial_update', 'destroy']:#put, patch. delete
#             permissions = [IsAuctionAuthor, ]
#         else:
#             permissions = [IsAuthenticated, ]
#         return [permission() for permission in permissions]



#     def get_queryset(self):
#         queryset=super().get_queryset()
#         weeks_count=int(self.request.query_params.get('days', 0))#query-params return dict
#         if weeks_count>0:
#             start_data=timezone.now()-timedelta(days=weeks_count)
#             queryset=queryset.filter(created_at__gte=start_data)#фильтрация по  полю created_at
#         return queryset
    
#     @action(detail=False, methods=['get'])
#     def own(self, request, pk=None):
#         queryset = self.get_queryset()
#         queryset = queryset.filter(user=request.user)
#         serializers =AuctionSerializer(queryset, many=True,
#                                        context={'request': request})
#         return Response(serializers.data, status=status.HTTP_200_OK)

    


#     @action(detail=False, methods=['get'])
#     def search(self, request, pk=None):
#         print(request.query_params)
#         q=request.query_params.get('q')
#         queryset=self.get_queryset()
#         queryset=queryset.filter(Q(title__icontains=q) |
#                                 Q(description__icontains=q))
#         serializer=AuctionSerializer(queryset, many=True, context={'request':request})
#         return Response(serializer.data, status=status.HTTP_200_OK)



# class AuctionImageView(generics.ListCreateAPIView):
#     queryset=AuctionImage.objects.all()
#     serializer_class=AuctionImageSerializer

#     def get_serializer_context(self):
#         return {'request':self.request}


# '--------------------------------------------------------------------------------'
# class AuctionUserView(generics.ListAPIView):
#     queryset=Bid.objects.all()
#     serializer_class=BidSerializer
#     # pagination_class=MyPaginationClass

#     def get_serializer_context(self):
#         return {'request':self.request}

# # '============================BID================================='



# class BidCreateView(APIView):   
     
#     def post(self, request, *args, **kwargs):
#         serializer = BidSerializer(data=request.data)
#         # print('DATA',request.data)
#         serializer.is_valid()
#         auction=Auction.objects.get(auction_id=request.data['auction'])
#         current_offer=auction.start_price
        
#         # print(float(request.data['offer']))
#         # print(float(current_offer))

#         bid_date= date.today()
#         # return Response('ok')
       
#         if  float(request.data['offer']) <= float(current_offer):
#             return Response("низкая стоимость ставки.",  status=status.HTTP_400_BAD_REQUEST) 
#         if  bid_date>auction.end_time:
#             return Response("аукцион истек.",  status=status.HTTP_400_BAD_REQUEST) 
        
#         auction.start_price=request.data['offer']
#         serializer.save()
#         auction.save()
#         return Response("Ставка создана.", status=status.HTTP_201_CREATED)



# # class BidDetailView(APIView):
    
# #     def get(self, request, *args, **kwargs):
# #         print(user_id=kwargs["user"])
# #         return Response('ok')
# #         # bids = Bid.objects.filter(user_id=kwargs["user"])
# #         # bids_serializers = BidSerializer(bids, many=True)
# #         # return Response(bids_serializers.data)

# class BidsView(APIView):#Работает
      
#       def get(self, request, *args, **kwargs):
#         bids=Bid.objects.all()
#         bids_serializers = BidSerializer(bids, many=True)
#         return Response(bids_serializers.data, status=status.HTTP_202_ACCEPTED)
    
# # class BidTopView(APIView):
      
# #       def get(self, request, *args, **kwargs):
    
# #         bids=Bid.objects.filter(user_id=self.kwargs["user"], auction_id=self.kwargs["auction"]).order_by('-offer')
# #         bids_serializers = BidSerializer(bids, many=True)
# #         return Response(bids_serializers.data, status=status.HTTP_202_ACCEPTED)

# # class BidDeleteView(generics.DestroyAPIView):

# #     def delete(self, request, *args, **kwargs):

# #         # print(user_id = request.user.id)
# #         auctions = kwargs['auction']
# #         users= kwargs['user']
# #         self.queryset = Bid.objects.filter(user_id=self.kwargs["user"],auction_id=int(kwargs['auction']))
        
# #         if  not self.queryset.exists():
# #             return Response("Нет ставки",  status=status.HTTP_400_BAD_REQUEST)

# #         self.queryset.delete() 
# #         return Response(f"Заявки на аукцион удалены{auctions} клиентом {users}",status=status.HTTP_200_OK) 


