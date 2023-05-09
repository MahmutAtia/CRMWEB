from django.db import models
from accounts.models import User
from django.contrib.auth import urls
from django_countries.fields import CountryField

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=128,blank=True)

    def __str__(self):
        return self.name



class Company(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=50 , unique=True)
    country = models.ForeignKey(Country,on_delete=models.CASCADE,null=True, blank=True )
    email = models.CharField(max_length=255,blank=True)
    phone = models.CharField(max_length=50,null=True, blank=True)
    website = models.CharField(max_length=255,blank=True,null=True)
    manager = models.CharField(max_length=128,null=True, blank=True)
    status = models.BooleanField( null=True, blank=True)
    def __str__(self):
        return self.name


class ContactType(models.Model):
    contact_type = models.CharField(max_length=20 )

    def __str__(self):
        return self.contact_type

class ContactResult(models.Model):  
    contact_result= models.CharField(max_length=20)

    def __str__(self):
        return self.contact_result

class Contact(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    typ = models.ForeignKey(ContactType,on_delete=models.SET_NULL , null=True)
    contact_time = models.CharField(max_length=10, null=True,blank=True)
    date = models.DateField( null=True,blank=True)   
    result = models.ForeignKey(ContactResult , on_delete= models.SET_NULL,null=True)
    class Meta:
        ordering= ["date"]

    def __str__(self):
        return  "\nCompany: " + self.company.name