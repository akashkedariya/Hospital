from django.urls import path
from .views import *
from App import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [

    path('user_register/',views.Register),
    path('user_login/',views.user_login, name = 'user_login'),
    path('user_logout/',views.user_logout, name = 'user_logout'),
    path('appoinment_request/',views.appoinment_request,name = 'appoinment_request'),
    path('doctor_detaile/',views.doctor_detaile,name = 'doctor_detaile'),
    path('patient_request_to_hoispital/',views.patient_request_to_hoispital,name = 'patient_request_to_hoispital'),
    path('appoinment_accept_reject/',views.appoinment_accept_reject),
    path('update_patient_detaile/',views.update_patient_detaile),
    path('add_medicine_detailes/',views.add_medicine_detailes),
    path('add_medicine/',views.add_medicine.as_view()),
    path('prescription_to_patient/',views.prescription_to_patient),
    path('doctor_prescriptionDetail/',views.Doctor_prescriptionDetail.as_view()),
    path('doctor_prescriptionDetail/<int:pk>/',views.Doctor_prescriptionDetail.as_view()),
    path('disribution_medicine_patient/',views.disribution_medicine_patient),
    # path('doctor_prescriptionDetail/',views.Doctor_prescriptionDetail.as_view()),
    # path('doctor_prescriptionDetail/',views.Doctor_prescriptionDetail.as_view()),
    # path('doctor_prescriptionDetail/',views.Doctor_prescriptionDetail.as_view()),


    # path('demo/',views.demo,name = 'demo'),


]