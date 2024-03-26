from django.urls import path
from cart.views import CartViewSet,CartDetailViewSet
urlpatterns = [
    path('item/',CartViewSet.as_view({'post':'create'})),
    path('item_get/',CartViewSet.as_view({'get':'get'})),
    path('item_delete/<int:pk>/', CartDetailViewSet.as_view({'delete': 'delete'})), 
]
