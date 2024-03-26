from django.db import models
from base.models import BaseModel
from django.utils.translation import gettext as _
# Create your models here.

class ProductCategory(BaseModel):
    product_name=models.CharField( max_length=100)
    slug=models.SlugField(max_length=100,blank=True,null=True,unique=True)
    image=models.ImageField()

    def __str__(self):
        return self.product_name
    

class ProductModel(BaseModel):
    product_name=models.CharField(_("title"), max_length=100)
    price=models.CharField( max_length=50)
    selling_price=models.FloatField(_("selling price"))
    slug=models.SlugField(_(""),max_length=100,blank=True,null=True,unique=True)
    discount=models.FloatField(_("discount"))
    description=models.TextField(_("description"))
    image=models.ImageField()
    categories=models.ManyToManyField(ProductCategory,blank=False)
    def __str__(self):
        return self.product_name
    
    