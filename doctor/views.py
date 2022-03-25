from django.shortcuts import render,redirect
from .models import *
from admins.models import *
from clinic.models import *
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def doc_login(req):
    if req.method =='POST':
        username= req.POST['username']
        password=req.POST['password']
        try:
            login_detail = DoctorDetails.objects.get(username=username)
            if login_detail.username == username and login_detail.password == password:
                    return render(req,'doc_home.html') 
        except DoctorDetails.DoesNotExist:
            return render(req,'doc_login.html',{'message':'Login Failed'})
    return render(req,'doc_login.html')
def doc_feedback(req):
    data = Contact.objects.all()
    return render(req,'doc_feedback.html',{'data':data})
def patient_list(req):
    info=Booking.objects.all()
    return render(req,'patient_list.html',{'info':info})
def doc_base(req):
    return render(req,'doc_base.html')
def doc_about(req):
    return render(req,'doc_about.html')
def doc_home(req):
    return render(req,'doc_home.html')
def doc_logout(req):
    print("1")
    logout(req)
    return redirect("doc_login")