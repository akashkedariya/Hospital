from django.contrib import admin
from .models import Patient_Appointment, CustomUser, Doctor_detaile, Patient_Detailes, Medical_shop, Doctor_prescription, medicine_distribution
# Register your models here.


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id','username','first_name','last_name','address','mobile','age','doctor','date_of_birth','gender','is_active','is_superuser','email','password']


@admin.register(Doctor_detaile)
class Doctor_detaileAdmin(admin.ModelAdmin):
    list_display = ['id', 'doctor_name','email','address','mobile','blood_group','age','date_of_birth','gender','Specialties','degree']


@admin.register(Patient_Appointment)
class Patient_AppointmentAdmin(admin.ModelAdmin):
    list_display = ['id','patient_detailes','appoinment_date','appoinment_time','doctor',"status"]

    # list_display = ['id', 'patient_name','email','address','mobile','blood_group','age','date_of_birth','gender','illnesses','appoinment_date','appoinment_time','doctor',"status"]


@admin.register(Patient_Detailes)
class Patient_detailesAdmin(admin.ModelAdmin) :
    list_display = ['id', "patient_name","email", "address","gender", "mobile","blood_group", "age", "date_of_birth","illnesses"]


@admin.register(Medical_shop)
class Medical_shopAdmin(admin.ModelAdmin):
    # list_display = ['id','tablet_id','tablet_name','company',"price", 'quantity']    
    list_display = ["tablet_id","tablet_name","company","price","quantity"]


@admin.register(Doctor_prescription) 
class Doc_prescripAdmin(admin.ModelAdmin):
    list_display = ['id','patient','prescription','adviced','provide']


@admin.register(medicine_distribution) 
class medicine_distributionAdmin(admin.ModelAdmin):
    list_display = ['id','patient','medicine','total_price']
