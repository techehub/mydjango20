
from django.urls import path
from .views import registerUser, loginUser

urlpatterns = [
    path ('register', registerUser),
    path('login', loginUser),

]
