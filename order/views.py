from urllib.request import Request
from django.shortcuts import get_object_or_404, render
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from order.models import *
from order.serializers import *
from rest_framework.permissions import IsAuthenticated
from cart.models import CartItem
from rest_framework.generics import ListAPIView
# Create your views here.

class OrderViewSet(ViewSet):
    permission_classes=[IsAuthenticated,]
    def create(self,request,*args, **kwargs):
        request.data["user"] = request.user.id
        serializer=OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={'status':'Sucess','message':'Order placed successfully'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request):
        order=Order.objects.filter(user=request.user)
        serializer=OrderViewSerializer(order,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    


class OrderCancellationAPIView(ViewSet):
    permission_classes = [IsAuthenticated]

    def cancle(self, request, user_id, order_id):
        user = get_object_or_404(User, id=user_id)
        order = get_object_or_404(Order, id=order_id, user=user)

        # Check if the order has already been canceled
        if order.status == 'Canceled':
            return Response({'message': 'This order has already been canceled'}, status=status.HTTP_400_BAD_REQUEST)

        # Cancel the order
        order.status = 'Canceled'
        order.save()

        return Response({'message': 'Order canceled successfully'}, status=status.HTTP_200_OK)