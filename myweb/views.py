
from django.http import  HttpResponse

def myhome (request):
    html = "<html>"\
           "<body bgcolor='blue'>"\
           "<h1> Welcome to my web site </h1> "\
                        "</body>"\
                        "</html>";
    return HttpResponse(html)


