from django.shortcuts import render

# Create your views here.

from django.http import  HttpResponse
from django.template import loader

def productdetails (r):
    template =loader.get_template("productdetail.html")
    data= {"name": "Samsung Note 10", "desc": "Samsung Smart phone"
           , "price" : 62000.00,
           "hgfaghS": ["4 GB Ram", "6 Inch Display", "23 MP Camera"]}

    return HttpResponse(template.render(data, r))
