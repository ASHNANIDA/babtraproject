from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate,login,logout

# from clinic.models import *
# Create your views here.
def admin_login(req):
    if req.method =='POST':
        username= req.POST['username']
        password=req.POST['password']
        try:
            user_details=AdminDetails.objects.get(username=username)
            if user_details.username==username and user_details.password==password:
                return render(req,'admin_base.html') 
        except AdminDetails.DoesNotExist:
            return render(req,'admin_login.html',{'message':'Login Failed'})
    return render(req,'admin_login.html')

def base(req):
    return render(req,'base.html')

def feedback(req):
    if req.method =='POST':
        subject= req.POST['subject']
        message=req.POST['message']
        print("worked")
        feed=AdminFeedback(subject=subject,message=message)
        feed.save()
    return render(req,'feedback.html')

def add_doctors(req):
    if req.method =='POST':
        username= req.POST['username']
        password=req.POST['password']
        firstname= req.POST['firstname']
        lastname= req.POST['lastname']
        email= req.POST['email']
        phone= req.POST['phone']
        qualification= req.POST['qualification']
        exp= req.POST['exp']
        image= req.POST['image']
        print("worked")
        doctor_details=DoctorDetails(username=username,password=password,firstname=firstname,lastname=lastname,email=email,phone=phone,qualification=qualification,experience=exp,image=image)
        doctor_details.save()
    return render(req,'add_doctors.html')
def admin_logout(req):
    logout(req)
    return redirect("admin_login")
