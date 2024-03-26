import django
from django.db import models
from base.models import BaseModel
from django.utils.translation import gettext as _
from authAPI.models import *
from productAPI.models import *
# Create your models here.


class Order(BaseModel):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Canceled', 'Canceled'),
    ]

    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE)
    status = models.CharField(_("Status"), max_length=20, choices=STATUS_CHOICES, default='Pending')


class OrderItem(BaseModel):
    order = models.ForeignKey(Order, verbose_name=_("Order"), on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(ProductModel, verbose_name=_("Product"), on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(_("Quantity"), default=1)