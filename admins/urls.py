from django.urls import path
from . import views
urlpatterns = [
    
    path('base/',views.base,name='base'),
    path('admin_login/',views.admin_login,name='admin_login'),
    path('feedback/',views.feedback,name='feedback'),
    path('add_doctors/',views.add_doctors,name='add_doctors'),
    path('admin_logout/',views.admin_logout,name='admin_logout'),

]