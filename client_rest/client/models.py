#id,name,contact,fees, fk= user
from django.db import models
from django.contrib .auth.models import User
# Create your models here.


class Client(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=30)
    retainer_fees = models.CharField(max_length=30)