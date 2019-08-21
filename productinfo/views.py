from django.shortcuts import render

# Create your views here.

from django.http import  HttpResponse



def productdetails (request):
    html = "<html>"\
           "<body bgcolor='red'>"\
           "<h1> This is my product details page </h1> "\
                        "</body>"\
                        "</html>";
    return HttpResponse(html)

