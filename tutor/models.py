from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=20, blank=True)
    password = models.CharField(max_length=20, blank=True)
    role = models.CharField(max_length=255,blank=True )
    skills = models.TextField(max_length=255,blank=True )
    email = models.CharField(max_length=255,blank=True )
    phone = models.IntegerField()