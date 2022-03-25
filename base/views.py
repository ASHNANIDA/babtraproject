from django.shortcuts import render
# Create your views here.
def start(req):
    return render(req,'start.html')
def base_about(req):
    return render(req,'base_about.html')
def base_logo(req):
    return render(req,'base_logo.html')
