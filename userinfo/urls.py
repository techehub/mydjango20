
from django.urls import path
from .views import registerUser, loginUser, contact, contactdata

urlpatterns = [
    path ('register', registerUser),
    path('login', loginUser),
    path ('contact', contact),
    path ('contactdata', contactdata)

]
