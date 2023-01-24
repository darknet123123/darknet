from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework import status
from .models import Cart, CartItem
from .serializers import CartItemSerializers, CartSerializers
from rest_framework.response import Response
from main.models import Product


class CartDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializers

    def retrieve(self, request, *args, **kwargs):
        queryset = Cart.objects.get_or_new(request)
        serializer = CartSerializers(queryset, context={'request': request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)

from rest_framework import generics
class CartItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializers

class CartItemView(CreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializers

    def post(self, request, *args, **kwargs):
        print(request.data)
        cartitem = CartItem.objects.all()
        product_item = Product.objects.get(pk=request.data['id'])
        # print(product_item)
        for item in cartitem:
            if item.product_item == product_item:
                return Response(data={'message': 'The product is already in the cart'},
                                status=status.HTTP_400_BAD_REQUEST)
            # if product_item.stock == 0 or int(request.data['amount']) > product_item.stock:
            #     return Response(data={'message': 'No enough stock'}, status=status.HTTP_400_BAD_REQUEST)
            if product_item.quantity == 0 or int(request.data['amount']) > product_item.quantity:
                return Response(data={'message': 'No enough quantity'}, status=status.HTTP_400_BAD_REQUEST)
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        cart = Cart.objects.get_or_new(self.request).first()
        serializer.save(cart=cart)


from rest_framework.decorators import api_view
@api_view(['GET'])
def session_get(request):
    print(request.session.get('cart'))
    return Response(data={"message": f"{request.session.get('cart')}"}, status=status.HTTP_200_OK)