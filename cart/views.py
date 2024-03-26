from django.shortcuts import render
from cart.serializers import CartItemSerializer,CartItemViewSerializer
from cart.models import CartItem,Cart
from authAPI.models import User
from productAPI.models import *
from productAPI.serializers import *
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet 
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
# Create your views here.

class CartViewSet(ViewSet):
    def create(self,request, *args, **kwargs):
        permission_classes=[IsAuthenticated,]
        request.data["user"] = request.user.id
        cart=CartItemSerializer(data=request.data)
        if cart.is_valid():
            cart.save()
            return Response({'message': 'Item added to cart successfully'})
        return Response(cart.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        model=Cart.objects.filter(user=request.user)
        serializer=CartItemViewSerializer(model,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

        
class CartDetailViewSet(CartViewSet):
    def delete(self, request, *args, **kwargs):
        try:
            cart_item = CartItem.objects.get(id=kwargs['pk'], cart__user=request.user)
            cart_item.delete()
            return Response({'message': 'Item deleted from cart successfully'}, status=status.HTTP_204_NO_CONTENT)
        except CartItem.DoesNotExist:
            return Response({'error': 'Item not found in cart'}, status=status.HTTP_404_NOT_FOUND)