from django.db import models
from student.models import *

# Create your models here.
class course_detailstable(models.Model):
  ctitle = models.CharField(max_length=10)
  clanguage=models.CharField(max_length=10)
  iname=models.CharField(max_length=10)
  clevel=models.CharField(max_length=10)
  ctime=models.CharField(max_length=10)
  cdetails=models.CharField(max_length=10)
  ccost = models.CharField(max_length=200)



class payment_detailstable(models.Model):
  cardtype = models.CharField(max_length=255)
  cardholdername=models.CharField(max_length=255)
  cardnumber=models.CharField(max_length=16)
  expirydate=models.CharField(max_length=255)
  cvv=models.CharField(max_length=3)

