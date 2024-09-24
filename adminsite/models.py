from django.db import models

# Create your models here.
class Admin_signup(models.Model):
    email1=models.CharField(max_length=25)
    password=models.CharField(max_length=25)
    name = models.CharField(max_length=25, primary_key=True)
    phone_number=models.IntegerField()

class Admin_login(models.Model):
     email=models.CharField(max_length=25,primary_key=True)
     password=models.CharField(max_length=25)

class job_details(models.Model):
    companyName=models.CharField(max_length=25)
    role=models.CharField(max_length=25)
    skills = models.CharField(max_length=25)
    salary=models.IntegerField()
    location=models.CharField(max_length=250)

class job_applicationmodel(models.Model):
    jobname=models.CharField(max_length=25)
    resume=models.FileField()
    


