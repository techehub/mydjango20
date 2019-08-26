from django.contrib import admin
from django.urls import path
from .views import  productdetails,productdetailsNew

urlpatterns = [
     path ('product/<int:pid>', productdetails),
     path('product_new', productdetailsNew)



]
