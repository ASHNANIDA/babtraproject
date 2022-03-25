from django.db import models

# Create your models here.
class Signup(models.Model):
   firstname=models.CharField(max_length=20)
   lastname=models.CharField(max_length=20)
   gender=models.CharField(max_length=20)
   address=models.TextField()
   email=models.EmailField(max_length=30)
   mobile=models.IntegerField()
   password=models.CharField(max_length=30, default=111111)

class Booking(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.BigIntegerField()
    email=models.CharField(max_length=50)
    dob=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    subject=models.CharField(max_length=60)
    message=models.TextField()


   