from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from authAPI.managers import UserManager
from django.utils.translation import gettext as _
from base.models import BaseModel
# Create your models here.

class User(AbstractBaseUser,PermissionsMixin):
    first_name=models.CharField(_("First name"), max_length=256)
    last_name=models.CharField(_("Last name"), max_length=256)
    email=models.EmailField(_("email"), max_length=100,unique=True)
    is_staff=models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)
    
    USERNAME_FIELD="email"
    REQUIRED_FIELDS=[]

    objects=UserManager()


    def __str__(self):
        return self.email
    
class Address(BaseModel):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    mobile_no=models.CharField(max_length=12)
    address1=models.CharField(_(""), max_length=250)
    address2=models.CharField(_(""), max_length=250)
    district=models.CharField(_(""), max_length=50)
    pincode=models.IntegerField(_(""))
    state=models.CharField(_(""), max_length=50)

    def __str__(self):
        return self.user.email
