from django.shortcuts import render
from django.shortcuts import render, HttpResponseRedirect, redirect
from .models import CustomUser , Patient_Appointment, Doctor_detaile, Patient_Detailes, Doctor_prescription, medicine_distribution, Medical_shop
# from .forms import CustomUserForm , BookForm, Filter_Form, IssuedBookForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login as log_user, logout as lgout
import datetime
from django.conf import settings
from django.core.mail import send_mail
from django.utils.dateparse import parse_datetime
from django.core.mail import EmailMultiAlternatives
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate , login , logout
from rest_framework import status
from rest_framework.decorators import api_view
from App.serializers import Medical_shopSerializer, Doc_presSerializer, medicine_distributionSerializer
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView




@csrf_exempt
def Register(request):
    print('==================Working')
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        address = request.POST["address"]
        mobile = request.POST["mobile"]
        # blood_group = request.POST["blood_group"]
        age = request.POST["age"]
        date_of_birth = request.POST["date_of_birth"]
        gender = request.POST["gender"]

        print('==========date_of_birth========Working',date_of_birth)

        email = request.POST["email"]
        if CustomUser.objects.filter(email=email).exists():
            print('=======email exist=====')
            return JsonResponse({"Email" : "Email already registered"})

        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1 == password2:
               
            user = CustomUser.objects.create(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                address=address,
                mobile= mobile,
                age=age,
                date_of_birth = date_of_birth,  
                gender = gender,
                password=password1
            )

            user.set_password(password1)
            user.save()

            subject, from_email, to = 'Your Account Registaration Sucessful', '', str(email)
            text_content = 'This is an important message.'
            html_content = '<body><h2>User registration to Sanjivani Hospital..,<h2><br> In Hospital </body>'
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            return JsonResponse({'User' : "User account Registaration Sucessfully"})
        
        else:           
            return JsonResponse({"Password" : "Password not matches"})
        


@csrf_exempt
def user_login(request):
   
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        
        user = authenticate(email=email, password=password)
        
        if user is not None:
            login(request, user)   
            return JsonResponse({'Login' : "User login successfully"})
        
        else:
            return JsonResponse({'Login' : "Invalid Credential"})


#    list_display = ['id', "patient_name","email", "address", "mobile","blood_group", "age", "date_of_birth","illnesses"]

@csrf_exempt
def patient_detailes(request):
    if request.method == 'POST':
        pass


        


@csrf_exempt
def user_logout(request) :
    if request.method == 'POST':
        logout(request)       

        return JsonResponse({'Logout' : "User logout successfully"})


@csrf_exempt        
def doctor_detaile(request) :
    if request.method == 'POST':
        print('========Working======')
    # list_display = ['id', 'doctor_name','email','address','mobile','blood_group','age','date_of_birth','gender','Specialties','degree']
        doctor_name = request.POST['doctor_name']
        address = request.POST['address']
        doctor = request.POST.get('doctor')
        mobile = request.POST["mobile"]
        blood_group = request.POST["blood_group"]
        age = request.POST['age']
        date_of_birth = request.POST["date_of_birth"]
        gender = request.POST["gender"]
        Specialties = request.POST["Specialties"]
        degree = request.POST["degree"]
        email = request.POST['email']
        # password = request.POST['Password']
        password = request.POST.get('password')
        password2 = request.POST['password2']

        if CustomUser.objects.filter(email=email).exists():
     
            return JsonResponse({"Email Validation" : "Email already exist"})
        

        if password != password2 :
            return JsonResponse({'Validation' : 'Password Not matched'})
        
        else :

            user = CustomUser.objects.create(          
                    first_name=doctor_name,
                    last_name=doctor_name,
                    username=doctor_name,
                    email=email,
                    address=address,
                    doctor = doctor,
                    mobile= mobile,
                    age=age,
                    date_of_birth = date_of_birth,  
                    gender = gender,
                    password=password2
                )
            user.set_password(password)
            user.save()

        Doctor_detaile.objects.create(doctor_name=doctor_name,
                                      email=email,
                                      address=address,
                                      mobile=mobile,
                                      blood_group=blood_group,
                                      age=age,
                                      date_of_birth=date_of_birth,
                                      gender=gender,
                                      Specialties=Specialties,
                                      degree=degree)
        
        return JsonResponse({'Doctor':'Doctor register successfully'})



@csrf_exempt
def patient_request_to_hoispital(request) : 
   # list_display = ['id', "patient_name","email", "address", "mobile","blood_group", "age", "date_of_birth","illnesses"]
    if request.method == "POST" :
        print('======user=====',request.user)

        blood_group = request.POST['blood_group']
        illnesses = request.POST['illnesses']

        user = CustomUser.objects.get(email=request.user)
        print('==========user===========',user.date_of_birth)
            

        Patient_Detailes.objects.create(

            patient_name = user.username,
            email = request.user,
            address = user.address,
            mobile = user.mobile,
            blood_group=blood_group,
            age = user.age,
            gender = user.gender,
            date_of_birth = user.date_of_birth, 
            illnesses = illnesses
        )

        return JsonResponse({'Patient Detailes':"Patient add successfully"})



@api_view(['GET', 'PUT', 'DELETE']) 
@csrf_exempt    
def update_patient_detaile(request):
    print('=====Working working=======')
    if request.method == 'PUT':

        patient_id = request.POST['patient_id']
        patient_name = request.POST['patient_name']
        # email = request.POST['email']
        address = request.POST['address']
        mobile = request.POST['mobile']
        blood_group = request.POST['blood_group']
        age = request.POST["age"]
        gender = request.POST["gender"]
        date_of_birth = request.POST['date_of_birth']
        illnesses = request.POST['illnesses']

        user = Patient_Detailes.objects.get(id=patient_id)
        print('=======user=========',user.email)

        Patient_Detailes.objects.filter(id = patient_id).update(patient_name=patient_name,
                                                                email=user.email,
                                                                address=address,
                                                                mobile=mobile,
                                                                blood_group=blood_group,
                                                                age=age,
                                                                date_of_birth=date_of_birth,
                                                                gender=gender,
                                                                illnesses=illnesses
                                                                )

        return JsonResponse({'Patient_Detailes':"Patient_Detailes update successfully"})


def get_doctor_detailes(self):
    if Patient_Appointment.objects.filter(doctor = self).exists():  
        data = Patient_Appointment.objects.get(doctor = self)
        return data
    # else:
    #     pass



@csrf_exempt
def appoinment_request(request):  
    if request.method == 'POST':
        print('=====Working=====')

        patient_detailes = request.POST.get("patient_detailes")
        appoinment_date = request.POST["appoinment_date"]
        appoinment_time = request.POST['appoinment_time']
        doctor = request.POST["doctor"] 

        data = Patient_Appointment.objects.all()

        for i in data :
           
            if str(i.doctor) == str(doctor) and str(i.appoinment_time) == str(appoinment_time) and str(i.appoinment_date) == str(appoinment_date):
               
                return JsonResponse({"Booked" : "This date and time has already appointed doctor "})
            
        patient_id = Patient_Detailes.objects.get(id=patient_detailes)
        doctor_id = Doctor_detaile.objects.get(id=doctor)
       
        Patient_Appointment.objects.create(patient_detailes = patient_id, 
                            appoinment_date = appoinment_date,
                            appoinment_time = appoinment_time,
                            doctor = doctor_id
                            )
        
        Patient_data = {
            "patient_id" : patient_detailes,
            "Patient name" : patient_id.patient_name,
            "appoinment_date" : appoinment_date,
            "appoinment_time" : appoinment_time,
            "doctor_id" : doctor,
            "doctor_name" : doctor_id.doctor_name

        }
        
        return JsonResponse({'Patient register' : "patient registered successfully",'Patient data':Patient_data})
    


@csrf_exempt
def appoinment_accept_reject(request):
    if request.method == 'POST':

        patient_id = request.POST["patient_id"]
        status = request.POST['status']  

        Patient_Appointment.objects.filter(id=patient_id).update(status=status)
        print('=========data=======',status) 

        return JsonResponse({'Request':'Appoinment Approved by doctor'})
    



@api_view(['GET',"POST"])
def add_medicine_detailes(request):

    if request.method == 'POST':
        data = request.data
        print('=======================data====',data['price'])
        serializer = Medical_shopSerializer(data=data)

        if serializer.is_valid():
            serializer.validated_data['price'] = 300 + int(data['price'])
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class add_medicine(APIView) :

    def post(request) :
        if request.method == 'POST' :
            data = request.data
            serializer = Medical_shopSerializer(data=data)

            if serializer.is_valid () :
                serializer.validated_data['price'] = 300 + int(data['price'])
                
                serializer.save()

                return Response(serializer.data, status=status.HTTP_201_CREATED)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET',"POST"])
def prescription_to_patient(request):
    
    if request.method == 'POST' :
        serializer = Doc_presSerializer(data = request.data)
    
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class Doctor_prescriptionDetail(APIView):
    
    def get_object(self,pk) :
        try:
            return Doctor_prescription.objects.get(id=pk)
        except Doctor_prescription.DoesNotExist:
            return HttpResponse(status=404)

    def get(self, request, pk=None, format=None):
        snippet = self.get_object(pk)

    # /    snippet = Doctor_prescription.objects.get(id=pk)
        serializer = Doc_presSerializer(snippet)
        # data_response = serializer.data
        # data_response['patient'] = 'Aanand'

        return Response(serializer.data)


    def put(self, request, pk, format=None):
        # snippet = self.get_object(pk)
        snippet = Doctor_prescription.objects.get(id=pk)
        serializer = Doc_presSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, pk, format=None):                                                                                 
    #     snippet = self.get_object(pk)   
    #     snippet.delete()   
    #     return Response(status=status.HTTP_204_NO_CONTENT)     
                                                                  

# @csrf_exempt
@api_view(['POST'])    
def disribution_medicine_patient(request):
    
    if request.method == 'POST' :
        
        data = request.data
        
        serializer = medicine_distributionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            medicine = Medical_shop.objects.get(tablet_id=str(data['medicine']))
            ud_medicine = medicine_distribution.objects.last()
            ud_medicine.total_price = medicine.price
            ud_medicine.save()
            data = medicine_distribution.objects.last()

            return JsonResponse(serializer.data, status=201)
        
        return JsonResponse(serializer.errors, status=400)


      
