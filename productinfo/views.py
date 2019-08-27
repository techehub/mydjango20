from django.shortcuts import render

# Create your views here.

from django.http import  HttpResponse
from django.template import loader
from .models import Product

def productdetails (request,pid):
    if request.session.__contains__("PID"):
        print ("Session PID:::", request.session.__getitem__("PID"))

    print(request.GET)
    print (">>>>>>>>>>>>>>>>>>>>"+ str (pid))

    product =  Product.objects.get(id=pid)

    data = {

        "name": product.pname, "desc": product.pdesc, "price": product.price,


    }

    print ("data is ", data)

    template =loader.get_template("productdetail.html")


    res = HttpResponse(template.render(data , request))

    res.set_cookie("lastaccessed", product.pid)

    if request.session.__contains__("PID"):
        request.session.__setitem__("PID", request.session["PID"] + ":"+ product.pid )


    else :
        request.session.__setitem__("PID" ,  product.pid )

    res.set_cookie("PIDs",request.session["PID"] )

    return res



def productdetails_old (request,pid):
    print(request.GET)
    print (request.GET["id"])
    print(request.GET["name"])
    print (">>>>>>>>>>>>>>>>>>>>"+ str (pid))

    template =loader.get_template("productdetail.html")
    data=  {

    "1": {"name": "Samsung Note 10", "desc": "Samsung Smart phone", "price" : 62000.00,"features": ["4 GB Ram", "6 Inch Display", "23 MP Camera"]
          },
    "2": {"name": "OPPO", "desc": "OPPO Phone", "price": 12000.00, "features": ["4 GB Ram", "5 Inch Display", "10 MP Camera"]}
    }


    return HttpResponse(template.render(data [str(pid)], request))




def productdetailsNew (request):

    pid= request.GET["id"]
    print (">>>>>>>>>>>>>>>>>>>>"+ str (pid))

    template =loader.get_template("productdetail.html")
    data=  {

    "1": {"name": "Samsung Note 10", "desc": "Samsung Smart phone", "price" : 62000.00,"features": ["4 GB Ram", "6 Inch Display", "23 MP Camera"]
          },
    "2": {"name": "OPPO", "desc": "OPPO Phone", "price": 12000.00, "features": ["4 GB Ram", "5 Inch Display", "10 MP Camera"]}
    }


    return HttpResponse(template.render(data [str(pid)], request))

