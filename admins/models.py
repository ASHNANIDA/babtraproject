from django.db import models

# Create your models here.
class AdminDetails(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=20)
    
class DoctorDetails(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=20)
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    phone=models.BigIntegerField()
    qualification=models.CharField(max_length=30)
    experience=models.CharField(max_length=30)
    image=models.CharField(max_length=100)
    
class AdminFeedback(models.Model):
    subject=models.CharField(max_length=50)
    message=models.TextField()