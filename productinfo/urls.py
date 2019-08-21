from django.contrib import admin
from django.urls import path
from .views import  productdetails

urlpatterns = [
     path ('product', productdetails)

]
