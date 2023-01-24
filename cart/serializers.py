# from .models import Cart, CartItem
# from rest_framework import serializers


# class CartItemSerializer(serializers.ModelSerializer):
#     price = serializers.ReadOnlyField(source='get_total_price')
#     #source мы используем чтобы получить результат функции прописаной в моделях

#     class Meta:
#         model = CartItem
#         fields = ('product', 'amount', 'price')


# class CartSerializer(serializers.ModelSerializer):
#     items = CartItemSerializer(many=True, write_only=True)

#     class Meta:
#         model = Cart
#         fields = ('id', 'items', )

#     def create(self, validated_data):
#         request = self.context.get('request')
#         print(request)
#         items = validated_data.pop('items')
#         user = request.user
#         cart = Cart.objects.create(user=user)
#         # пройтись циклом чтобы достать продукты из списка CartItem
#         for item in items:
#             CartItem.objects.create(cart=cart, product=item['product'], amount=item['amount'])
#         return cart

#     def to_representation(self, instance):
#         representation = super(CartSerializer, self).to_representation(instance)
#         representation['products'] = CartItemSerializer(instance.items.all(), many=True).data
#         return representation

from rest_framework import serializers
from .models import Cart, CartItem


class CartSerializers(serializers.ModelSerializer):
    """Get Cart list"""

    class Meta:
        model = Cart
        fields = ('id', 'user', 'cart_items',)


class CartItemSerializers(serializers.ModelSerializer):
    """Get CartItem List"""

    class Meta:
        model = CartItem
        fields = ('amount', 'product_item',)