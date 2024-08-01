from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager 
from django.utils.translation import gettext_lazy as _
from datetime import date
from django.utils import timezone
# from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, MaxValueValidator


class Usermanager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):  
 
        if not email:  
            raise ValueError(('The Email must be Required'))  
        email = self.normalize_email(email)  
          
        user = self.model(email=email, **extra_fields)  
        user.set_password(password)  
        user.save(using=self._db)
        return user 
                                              
    
    def create_superuser(self, email, password, **extra_fields): 
        extra_fields.setdefault('is_staff', True)  
        extra_fields.setdefault('is_superuser', True)  
        extra_fields.setdefault('is_active', True) 

        if extra_fields.get('is_staff') is not True:  
            raise ValueError(('Superuser must have is_staff=True.'))
        
        return self.create_user(email, password, **extra_fields)
    

GENDER_CHOICES = [
    ("male", "male"),
    ("female", "female"),
    ("other","other")

]

class CustomUser(AbstractUser):
    username = models.CharField(max_length=50) 
    address = models.CharField(max_length = 200)
    email = models.EmailField(max_length=200, unique=True)
    is_active = models.BooleanField(default=True)
    mobile = models.BigIntegerField(validators=[MinValueValidator(1000000000), MaxValueValidator(9999999999)],null=True)
    # blood_group = models.CharField(max_length = 50,null=True)
    age = models.IntegerField(null=True)
    date_of_birth = models.DateField(null=True)
    gender = models.CharField(max_length=30, choices=GENDER_CHOICES, null=True)
    doctor = models.BooleanField(default = False,null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = Usermanager()  

    def __str__(self) :
        return self.email


type_CHOICES = [
    
    ("Neurologist", "Neurologist"),
    ("Cardiologist", "Cardiologist"),
    ("Surgeon","Surgeon"),
    ("Radiologist","Radiologist"),
    ("nurse","nurse"),
    ("other" , "other")

]

GENDER_CHOICES = [
    ("male", "male"),
    ("female", "female"),
    ("other","other")

]


class Doctor_detaile(models.Model):
    # doctor_name = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True)
    doctor_name = models.CharField(max_length = 200)
    address = models.CharField(max_length = 200)
    email = models.EmailField(max_length=200, unique=True)
    gender = models.CharField(max_length=30, choices=GENDER_CHOICES, null=True)
    mobile = models.BigIntegerField(validators=[MinValueValidator(1000000000), MaxValueValidator(9999999999)],null=True)
    blood_group = models.CharField(max_length = 50,null=True)
    age = models.IntegerField(null=True)
    date_of_birth = models.DateField(null=True)
    Specialties = models.CharField(max_length=30, choices=type_CHOICES, null=True)    
    degree = models.CharField(max_length = 200)

    def __str__(self):
        return str(self.id) 
    

class Patient_Detailes(models.Model):  
    patient_name = models.CharField(max_length = 50)
    address = models.CharField(max_length = 200)
    email = models.EmailField(max_length=200)
    mobile = models.BigIntegerField(validators=[MinValueValidator(1000000000), MaxValueValidator(9999999999)],null=True)
    blood_group = models.CharField(max_length = 50,null=True)
    age = models.IntegerField(null=True)
    date_of_birth = models.DateField(null=True)
    gender = models.CharField(max_length=30, choices=GENDER_CHOICES, null=True)    
    illnesses = models.CharField(max_length = 500)
    
    def __str__(self) :
        return self.patient_name


GENDER_CHOICES = [
    ("male", "male"),
    ("female", "female"),
    ("other","other")

]
STATUS = [
    ("Pending","Pending"),
    ("Approved","Approved"),
    ("Rejected","Rejected")
]

  
from django.utils import timezone
class Patient_Appointment(models.Model):  
    patient_detailes = models.ForeignKey(Patient_Detailes, on_delete=models.CASCADE,null=True)
    appoinment_date = models.DateField(null = True, default='')
    appoinment_time = models.TimeField(null=True, blank=True)
    doctor = models.ForeignKey(Doctor_detaile, on_delete = models.CASCADE,null=True)
    status = models.CharField(max_length=30,choices=STATUS , default = "Pending",null=True) 

    def __str__(self) :
        return str(self.patient_detailes)
    


class Medical_shop(models.Model):

    tablet_id = models.AutoField(primary_key=True) 
    # tablet_id = models.CharField(max_length=40)
    tablet_name = models.CharField(max_length=90)
    company = models.CharField(max_length=50)
    price = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self) :
        return str(self.tablet_id)


class Doctor_prescription(models.Model):
    patient = models.ForeignKey(Patient_Appointment,on_delete=models.CASCADE,null=True, blank = True)
    prescription = models.CharField(max_length=500, blank = True)
    adviced = models.CharField(max_length = 300, blank = True)
    provide = models.BooleanField(default = False)
    # total_price = models.IntegerField(blank = True)

    def __str__(self):
        return str(self.patient)



class medicine_distribution(models.Model) :
    
    patient = models.ForeignKey(Doctor_prescription,on_delete = models.CASCADE,blank=True, null = True)
    medicine = models.ForeignKey(Medical_shop,on_delete = models.CASCADE, blank =True,null = True)
    total_price = models.IntegerField(null = True, blank = True)
    



    

    











