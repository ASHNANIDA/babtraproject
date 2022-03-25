from django.urls import path
from . import views
urlpatterns = [
    path('doc_login/',views.doc_login,name='doc_login'),
    path('doc_base/',views.doc_base,name='doc_base'),
    path('doc_home/',views.doc_home,name='doc_home'),
    path('doc_about/',views.doc_about,name='doc_about'),
    path('patient_list/',views.patient_list,name='patient_list'),
    path('doc_feedback/',views.doc_feedback,name='doc_feedback'),
    path('doc_logout/',views.doc_logout,name='doc_logout'),


]