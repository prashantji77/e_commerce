from django.db import models
from productAPI.models import *
from productAPI.serializers import *
from authAPI.models import User
from base.models import BaseModel
from django.utils.translation import gettext as _

# Create your models here.

class Cart(BaseModel):
    user = models.OneToOneField(User, verbose_name=_("User"), on_delete=models.CASCADE,unique=True)
    updated_at=models.DateTimeField(_(""), auto_now=True,null=True)

class CartItem(BaseModel):
    cart=models.ForeignKey(Cart, verbose_name=_(""), on_delete=models.CASCADE)
    product=models.ForeignKey(ProductModel, verbose_name=_(""), on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(_(""),default=1)
    updated_at=models.DateTimeField(_(""), auto_now=True,null=True)