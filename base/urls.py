from django.urls import path
from . import views
urlpatterns = [
        path('start/',views.start,name='start'),
        path('base_about/',views.base_about,name='base_about'),
        path('base_logo/',views.base_logo,name='base_logo'),


]