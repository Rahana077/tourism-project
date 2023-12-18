from django.db import models

# Create your models here.
class customerdb(models.Model):
    cname=models.CharField(max_length=50,null=True,blank=True)
    cimage=models.ImageField(upload_to="categoryImage",null=True,blank=True)
    members =models.IntegerField(null=True,blank=True)
    address=models.CharField(max_length=50,null=True,blank=True)
    mobileno=models.IntegerField(null=True,blank=True)
    location=models.CharField(max_length=50,null=True,blank=True)

class destinationdb(models.Model):

    name=models.CharField(max_length=50,null=True,blank=True)
    price = models.IntegerField(null=True, blank=True)
    descrip = models.CharField(max_length=50, null=True,blank=True)
    img=models.ImageField(upload_to='product image',null=True,blank=True)
    lo=models.CharField(max_length=100,null=True,blank=True)


