from django.urls import path
from order.views import OrderViewSet,OrderCancellationAPIView

urlpatterns = [
    path(
        'order/',OrderViewSet.as_view({'post':'create'}),
    ),
    path(
        'order_list/',OrderViewSet.as_view({'get':'get'})
    ),
    path('order/<int:user_id>/<int:order_id>/cancel/', OrderCancellationAPIView.as_view({'post':'cancle'}), name='order-cancel'),
]
