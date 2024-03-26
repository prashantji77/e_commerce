from django.forms import SlugField
from productAPI.models import *
from rest_framework import serializers
from base.services import slugify

class ProductCategorySerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    uuid=serializers.UUIDField(read_only=True)
    product_name=serializers.CharField(max_length=100)
    image=serializers.ImageField(required=False,allow_null=True)

    def validate(self,attrs):
        if "product_name" in attrs.keys():
            product_name=attrs.get("product_name")
            attrs["slug"] =slugify(product_name)
        return attrs
    
    def create(self,validated_data):
        return ProductCategory.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        for key in validated_data.keys():
            setattr(instance,key,validated_data[key])
        instance.save()
        return instance
    
class ProductSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    uuid=serializers.UUIDField(read_only=True)
    slug=serializers.SlugField(read_only=True)
    product_name=serializers.CharField(max_length=100)
    discount=serializers.FloatField()
    selling_price=serializers.FloatField()
    price=serializers.CharField(max_length=50)
    categories=serializers.PrimaryKeyRelatedField(queryset=ProductCategory.objects.all(),many=True)
    image=serializers.ImageField()

    def validate(self,attrs):
        if "product_name" in attrs.keys() :
            product_name=attrs.get("product_name")
            attrs["slug"]=slugify(product_name)
        return attrs
    
    def get_categories(self,instance):
        categories=ProductCategory.objects.filter(id_in=instance.categories)
        return ProductCategorySerializer(categories)
    
    def create(self,validate_data):
        categories=validate_data.pop("categories")
        product_obj=ProductModel.objects.create(**validate_data)
        for category in categories:
            product_obj.categories.add(category)
        product_obj.save()
        return product_obj

    def update(self,instance,validate_data):
        for key in validate_data.keys():
            setattr(instance,key,validate_data[key])
            instance.save()
            return instance

