from functools import partial
from django.shortcuts import render
from authAPI.serializers import UserSeriaizer,UserAddressSerializer
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from authAPI.models import User ,Address
# Create your views here.

class UserApiViewSet(ViewSet):
    serializer_class=UserSeriaizer
    def create(self,request):
        serializer=UserSeriaizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST,data=serializer.errors)
    

class AddressApiViewSet(ViewSet,ListAPIView):
    serializer_class=UserAddressSerializer
    permission_classes=[IsAuthenticated,]

    def get_queryset(self):
        return Address.objects.filter(user=self.request.user)
    
    def create(self,request,formt=None):
        data=request.data
        data['user']=request.user.id
        serializer=self.get_serializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED) 
    
    def update(self,request,pk):
        instance=Address.objects.filter(pk=pk).first()
        if not instance:
            return Response(status=status.HTTP_204_NO_CONTENT,data={'message':'Address does not exist'})
        serializer=self.get_serializer(data=request.data,instance=instance,partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)



