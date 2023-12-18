from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class userregistrationdb(models.Model):
    uname=models.CharField(max_length=50,null=True,blank=True)
    upass=models.CharField(max_length=50,null=True,blank=True)

class Payment(models.Model):

    destname=models.CharField(max_length=100)

    due=models.CharField(max_length=100)
    locatn=models.IntegerField(null=True)
    dueprice = models.CharField(max_length=100,null=True)
    price = models.IntegerField(null=True)

class bookingdb(models.Model):
    destination_place = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    joining_place=models.CharField(max_length=100)
    departure_date = models.CharField(max_length=100,null=True)

    mobile=models.IntegerField(null=True)
    members=models.CharField(max_length=100)
    package = models.IntegerField(null=True)

class feedbackdb(models.Model):
    user=models.CharField(max_length=100,null=True,blank=True)
    feedback=models.CharField(max_length=50,null=True,blank=True)

class history(models.Model):
    users= models.CharField(max_length=100,null=True,blank=True)
    des_place =models.CharField(max_length=100,null=True)
    rating=models.IntegerField(null=True)










