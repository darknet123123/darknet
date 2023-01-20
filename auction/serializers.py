# from .models import *
# from rest_framework import serializers


# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model=AuctionCategory
#         fields="__all__"

# class AuctionSerializer(serializers.ModelSerializer):
#     start_time=serializers.DateTimeField(format="%d/%m/%Y  %H:%M:%S", read_only=True)
#     end_time=serializers.DateTimeField(format="%d/%m/%Y  %H:%M:%S", read_only=True)
    
#     class Meta:
#         model = Auction
#         fields = ['auction_id', 'title', 'description', 'category', 'start_price','start_time', 'end_time']

#     def to_representation(self, instance):
#         print(instance)
#         representation = super().to_representation(instance)
#         # representation['user']=instance.user.email
#         representation['category']=CategorySerializer(instance.category).data
#         representation['images'] = AuctionImageSerializer(instance.images.all(), many=True, context=self.context).data
#         return representation
       


# class BidSerializer(serializers.ModelSerializer):
#     # bid_id=serializers.DateTimeField(format="%d/%m/%Y  %H:%M:%S", read_only=True)
#     class Meta:
#         model = Bid
#         fields = ['bid_id',  'offer', 'auction', 'bid_time', 'product_sold']

# #Отображение Автора нкциона должен был быть

#     def to_representation(self, instance):
#         print(instance)
#         representation = super().to_representation(instance)
#         representation['user']=instance.user.email
#         return representation

    
#     def create(self, validated_data):
#         request = self.context.get('request')
#         user_id = request.user.id
#         validated_data['user_id'] = user_id
#         product= Auction.objects.create(**validated_data)
#         return  product







# '-------------------------Image--------------------------------'
# class AuctionImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=AuctionImage
#         fields="__all__"

    
#     def _get_image_url(self, obj):
#         if obj.image:
#             url=obj.image.url
#             request=self.context.get('request')

#             if request is not None:
#                 url=request.build_absolute_uri(url)
#         else:
#             url=''
#         return url

#     def to_representation(self, instance):
#         representation=super().to_representation(instance)
#         representation['image']=self._get_image_url(instance)
#         return representation

