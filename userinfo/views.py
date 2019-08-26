from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactUsForm
from .models import Conatct


# Create your views here.
def registerUser (request) :
    return HttpResponse ("This is my register page")



# Create your views here.
def loginUser (request) :
    return HttpResponse ("This is my login page")

def contact (request):
    form = ContactUsForm();
    return render(request, 'mycontactus.html', {'myform': form});

def  contactdata(request):

    c1= Conatct ( name= request.POST["name"],
              email=  request.POST["email"],
              phone=  request.POST["phone"],
              message=  request.POST["message"])

    c1.save()

    return render(request, 'contact_success.html', {});

