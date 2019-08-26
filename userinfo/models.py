from django.db import models

# Create your models here.


from django.db import models

class Conatct (models.Model):
   name = models.CharField(max_length=100)
   phone = models.CharField(max_length=100)
   email = models.EmailField()
   message=  models.CharField(default="", max_length=100)

   def __str__(self):
       return self.name  + ":" +self.email