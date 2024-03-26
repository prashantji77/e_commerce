from django.urls import path
from .views import ProductCategoryViewSet,ProductViewSet 
urlpatterns = [
    path(
        "product/",ProductViewSet.as_view({'post':'create'})
    ),

    path(
        "product/<uuid:product_uuid>/",ProductViewSet.as_view({'get':'get_product','patch':'update','delete':'delete'})
    ),

    path(
        "product/<str:slug>/view/",ProductViewSet.as_view({'get':'product_detail'})
    ),

    path(
        "product-category/",ProductCategoryViewSet.as_view({'get':'get_queryset','post':'create'})
    ),
    path(
        "product_all/",ProductViewSet.as_view({'get':'get'})
    ),
]
