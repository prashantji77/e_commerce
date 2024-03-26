from django.shortcuts import render
from base.models import *
from productAPI.models import *
from productAPI.serializers import *
from rest_framework.viewsets import ViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import BasePermission,SAFE_METHODS,IsAuthenticated
# Create your views here.
ADMIN_HTTP_METHOD=['POST','PUT','DELETE','PATCH']

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.method in  SAFE_METHODS:
                return True
            if request.method in ADMIN_HTTP_METHOD and request.user.is_admin:
                return True
        return False

class ProductViewSet(ViewSet):

    permission_classes=[ReadOnly,]

    def get(self,request,format=True):
        product=ProductModel.objects.all()
        serializer=ProductSerializer(product,many=True)
        return Response(serializer.data)
    
    def get_product(self,request,product_uuid):
        product=ProductModel.objects.get(uuid=product_uuid)
        serializer=ProductSerializer(product)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def create(self,request,format=True):
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def update(self , request,product_uuid):
        product=ProductModel.objects.get(uuid=product_uuid)
        serializer=ProductSerializer(product,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,product_uuid):
        product=ProductModel.objects.get(uuid=product_uuid)
        product.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    def product_detail(self,request,slug):
        product=ProductModel.objects.filter(slug=slug).last()
        serializer=ProductSerializer(product)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class ProductCategoryViewSet(ViewSet):

    permission_classes=[ReadOnly,]

    serializer_class=ProductCategorySerializer

    def get_queryset(self):
        product=ProductCategory.objects.get()
        return product

    def create(self,request):
        serializer=ProductCategorySerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
    
    


    

