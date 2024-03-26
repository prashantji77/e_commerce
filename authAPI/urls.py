from django.urls import path
from authAPI.views import *
from rest_framework_simplejwt.views import TokenObtainPairView 
from .views import UserApiViewSet,AddressApiViewSet
urlpatterns = [
    path("login/",TokenObtainPairView.as_view()),
    path('register/',UserApiViewSet.as_view({'post':'create'})),
    path('address/',AddressApiViewSet.as_view({'post':'create'})),
    path('address/<int:pk>/',AddressApiViewSet.as_view({'patch':'update'}))

]
