from django.db import models

# Create your models here.


class Product (models.Model):
    pid = models.CharField(max_length=10)
    pname= models.CharField(max_length=100)
    pdesc= models.CharField(max_length=250)
    features= models.CharField(max_length=500, default="")
    price= models.IntegerField()

    def __str__(self):
        return self.pid + ":"+ self.pname

