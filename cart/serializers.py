from re import S
from rest_framework import serializers
from authAPI.models import User
from django.utils import timezone
from productAPI.models import *
from productAPI.serializers import *
from cart.models import Cart,CartItem
from django.core.exceptions import ObjectDoesNotExist,ValidationError


class CartItemSerializer(serializers.Serializer):

    product = serializers.SlugRelatedField(
        slug_field='uuid',
        queryset=ProductModel.objects.all()
    )
    quantity = serializers.IntegerField()
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), 
        write_only=True
    )

    def create(self, validated_data):
        user = validated_data.pop('user')
        product = validated_data.pop('product')
        quantity = validated_data.pop('quantity')

        try:
            cart = Cart.objects.get(user=user)

        except ObjectDoesNotExist:
            cart = Cart.objects.create(user=user)

        try:
            cart_item = CartItem.objects.get(cart=cart, product=product)
            cart_item.quantity += quantity
            cart_item.save()
        except ObjectDoesNotExist:
            cart_item = CartItem.objects.create(cart=cart, product=product, quantity=quantity)

        return cart_item
    
  
class ViewSerializer(serializers.Serializer):
    product_id=serializers.PrimaryKeyRelatedField(queryset=ProductModel.objects.all())
    product=serializers.SlugRelatedField(
        slug_field="product_name",
        queryset=ProductModel.objects.all()   
    )
    quantity=serializers.IntegerField()

class CartItemViewSerializer(serializers.Serializer):
    created_at=serializers.DateTimeField()
    cart_item=serializers.SerializerMethodField()

    def get_cart_item(self,instance):
        cart_item=CartItem.objects.filter(cart=instance)
        return ViewSerializer(cart_item,many=True).data


