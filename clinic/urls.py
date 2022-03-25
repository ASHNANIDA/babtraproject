from django.urls import path
from . import views
urlpatterns = [
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('base/',views.base,name='base'),
    path('sendEmail/',views.sendEmail,name='sendEmail'),
    path('head/',views.head,name='head'),
    path('home/',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('team/',views.team,name='team'),
    path('booking/',views.booking,name='booking'),
    path('contact/',views.contact,name='contact'),
    path('payment/',views.payment,name='payment'),
    path('tracker/',views.tracker,name='tracker'),
    path('logout_req/',views.logout_req,name='logout_req'),

]