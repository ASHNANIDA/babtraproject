from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from random import randint
from django.core.mail import send_mail
from .models import *
from admins.models import *
from django.contrib.auth import login,logout
from django.contrib.auth import get_user_model
from django_email_verification import sendConfirm
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def login(req):
    print("worked")
    if req.method =='POST':
        email= req.POST['email']
        password=req.POST['password']
        print(email)
        print(password)
        try:
            obj1=Signup.objects.get(email=email)
            print("checked")
            if obj1.email == email and obj1.password == password:
                print("1")
                req.session["logged_user"]=obj1.id
                print(req.session)
                return redirect("home") 
        except Signup.DoesNotExist:
            return render(req,'login.html')
    return render(req,'login.html')       
    
def base(req):
    return render(req,'base.html')
def home(req):
    context=Signup.objects.all()
    return render(req,'home.html', {'context':context})
def signup(req):
    if req.method =='POST':
        firstname= req.POST['firstname']
        print(firstname)
        lastname= req.POST['lastname']
        gender=req.POST['gender']
        address=req.POST['address']
        email= req.POST['email']
        password=req.POST['password']
        mobile=req.POST['mobile']
    
        #generate otp
        # otp= randint(1000,9999)
        #send mail
        # a=send_mail('otp verification for registration', str(otp), 'ashnanidaharis@gmail.com', [userdata.email],fail_silently=False,)
        customer=Signup(firstname=firstname,lastname=lastname,gender=gender,email=email,mobile=mobile,address=address,password=password)
        customer.save()

    return render(req,'signup.html')

def team(req):
    doctor=DoctorDetails.objects.all()
    return render(req,'team.html',{'data':doctor})
def booking(req):
    print("wat")
    if req.method =='POST':
        name=req.POST['name']
        print(name)
        mobile=req.POST['mobile']
        email= req.POST['email']
        dob= req.POST['dob']
        gender= req.POST['gender']
        obj1=Booking(name=name,email=email,mobile=mobile,dob=dob,gender=gender)
        obj1.save()
        return redirect("payment")
    return render(req,'booking.html')
def about(req):
    return render(req,'about.html')
def contact(req):
    print("start")
    if req.method =='POST':
        name=req.POST['name']
        email= req.POST['email']
        subject=req.POST['subject']
        message= req.POST['message']
        print(name)
        obj1=Contact(name=name,email=email,subject=subject,message=message)
        print("worked")
        obj1.save()
    return render(req,'contact.html')
def payment(req):
    return render(req,'payment.html')
def tracker(req):
    return render(req,'tracker.html')
def head(req):
    return render(req,'head.html')
@csrf_exempt
def sendEmail(req):
    password=req.POST['password']
    username=req.POST['username']
    email= req.POST['email']
    user= get_user_model().objects.create(username=username,password=password,email=email)
    send confirm(user)
    return render(req,'confirm_template.html')
def logout_req(req):
    logout(req)
    return redirect("login")