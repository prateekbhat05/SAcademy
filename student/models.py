from django.db import models
from course.models import *

# Create your models here.
class Test(models.Model):
    testid = models.CharField(max_length=10, primary_key=True)
    tname = models.CharField(max_length=200, null=True, blank=True)
    tdate = models.DateField(null=True, blank=True)
    ttime = models.TimeField(null=True, blank=True)
    


class Student_register(models.Model):
    sid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)  
    # gender = models.CharField(max_length=10, null=True, blank=True)  
    highest_qualification = models.CharField(max_length=100, null=True, blank=True) 
    phone_no = models.CharField(max_length=15, null=True, blank=True)  
    email = models.EmailField(max_length=254, null=True, blank=True) 
    role = models.CharField(max_length=255,blank=True) 
    username = models.CharField(max_length=20, null=True, blank=True)
    password = models.CharField(max_length=20, null=True, blank=True)
    
class Student_login(models.Model):   
    username = models.CharField(max_length=20, null=True, blank=True)
    password = models.CharField(max_length=20, null=True, blank=True)

