from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def registerUser (request) :
    return HttpResponse ("This is my register page")



# Create your views here.
def loginUser (request) :
    return HttpResponse ("This is my login page")