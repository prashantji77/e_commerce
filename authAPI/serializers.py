from wsgiref.validate import validator
from authAPI.managers import UserManager
from rest_framework import serializers
from authAPI.models import User,Address
from django.utils.translation import gettext as _ 
from rest_framework.validators import UniqueValidator

class UserSeriaizer (serializers.Serializer):
    first_name=serializers.CharField(max_length=256)
    last_name=serializers.CharField(max_length=256)
    email=serializers.EmailField(max_length=100,validators=[UniqueValidator(queryset=User.objects.all())])
    password=serializers.CharField(max_length=50,write_only=True)


    def create(self,validate_data):
        password=validate_data.pop("password")
        user=User.objects.create(**validate_data)
        user.set_password(password)
        user.save()
        return validate_data

class UserAddressSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    user=serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    mobile_no=serializers.CharField(max_length=12)
    address1=serializers.CharField(max_length=250)
    address2=serializers.CharField(max_length=250,allow_blank=True,required=False)
    district=serializers.CharField(max_length=50)
    pincode=serializers.CharField(max_length=6)
    state=serializers.CharField(max_length=50)

    def create(self,validate_data):
        return Address.objects.create(**validate_data)
    
    def update(self,instance,validate_data):
        for key in validate_data.keys():
            setattr(instance,key,validate_data[key])
        instance.save()
        return instance

