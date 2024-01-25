from django.shortcuts import render,redirect
from django.urls import reverse
from .models import *
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages
# Create your views here.

def register(request):
    data = userRegister.objects.all()

    if request.method == "POST":
        company_name = request.POST.get('company_name')
        CIN_number = request.POST.get('CIN_number')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        telephone_number = request.POST.get('telephone_number')
        address = request.POST.get('address')
        zip_code = request.POST.get('zip_code')
        country = request.POST.get('country')
        password = request.POST.get('password')
        check_password= request.POST.get('check_password')


        special_chars = set('!@#$%^&*')
        if len(password) < 7:
            messages.error(request,"At least 7 characters required")
            return redirect('/register/')

        if not any(char.isdigit() for char in password):
            messages.error(request,"Password must contain numbers")
            return redirect('/register/')

        if not any(char in special_chars for char in password):
            messages.error(request,"Password must contain special characters: !@#$%^&*")
            return redirect('/register/')
        if password != check_password:
            messages.error(request,"Passwords do not match")
            return redirect('/register/')
        
        queryset = userRegister(company_name=company_name,CIN_number=CIN_number,first_name=first_name,last_name=last_name,telephone_number=telephone_number,address=address,zip_code=zip_code,country=country,password=make_password(password))
        queryset.save()
        return render(request,'register.html')


    return render(request,'register.html')


def login(request):

    if request.method == 'POST':
        company_name = request.POST.get('company_name')
        password = request.POST.get('password')


        if userRegister.objects.get(company_name=company_name):
            data = userRegister.objects.get(company_name=company_name)
            if check_password(password,data.password):
                return redirect(reverse('application_register',kwargs={'company_name':company_name}))
            else:
                messages.error(request,'wrong password')
                return redirect('/login/')
        else:
            messages.error(request,'user not detected')
            return redirect('/login/')
        
    return render(request,'login.html')


def application_register(request,company_name):
    company_name = userRegister.objects.get(company_name=company_name)
    if request.method == 'POST':
        model_name= request.POST.get('model_name')
        certificate_type= request.POST.get('certificate_type')
        vehicle_or_part= request.POST.get('vehicle_or_part')
        vehicle_type= request.POST.get('vehicle_type')
        description= request.POST.get('description')
        specification= request.FILES.get('specification')
        design= request.FILES.get('design')
        blueprint= request.FILES.get('blueprint')

        queryset = ApplicationRegistration(company_name=company_name,model_name=model_name,certificate_type=certificate_type,vehicle_or_part=vehicle_or_part,vehicle_type=vehicle_type,description=description,specification=specification,design=design,blueprint=blueprint)
        queryset.save()
    return render(request,'application_register.html',{"company_name":company_name})


def parameter_form(request,company_name,model_name):

    company_name = userRegister.objects.get(company_name=company_name)
    model_name = ApplicationRegistration.objects.get(model_name=model_name)
    if request.method == 'POST':
        
        dimensions= request.POST.get('dimensions')
        passenger= request.POST.get('passenger')
        engine_type= request.POST.get('engine_type')
        fuel_consumpsion= request.POST.get('fuel_consumpsion')
        alternate_fuel_consumption= request.POST.get('alternate_fuel_consumption')
        airbags_count= request.POST.get('airbags_count')
        infotainment_system= request.POST.get('infotainment_system')
        gears_type= request.POST.get('gears_type')
        car_type= request.POST.get('car_type')
        ADAS = request.POST.get('ADAS')
        Safety_Ratings= request.POST.get('Safety_Ratings')
        environment_safety= request.POST.get('environment_safety')
        Performance_Ratings= request.POST.get('Performance_Ratings')
        Fuel_Efficiency_Ratings= request.POST.get('Fuel_Efficiency_Ratings')


        queryset = FourWheelerParameter(company_name=company_name,model_name=model_name,dimensions=dimensions,passenger=passenger,engine_type=engine_type,fuel_consumpsion=fuel_consumpsion,alternate_fuel_consumption=alternate_fuel_consumption,airbags_count=airbags_count,infotainment_system=infotainment_system,gears_type=gears_type,car_type=car_type,ADAS=ADAS,Safety_Ratings=Safety_Ratings,environment_safety=environment_safety,Performance_Ratings=Performance_Ratings,Fuel_Efficiency_Ratings=Fuel_Efficiency_Ratings)        
        queryset.save()

    return render(request,'test_form.html')


def rating_certificate(request,model_name):
    data = FourWheelerParameter.objects.get(model_name=model_name)
    return render(request,'print_certificate.html',{'data':data}) 


def application_list(request):
    data = ApplicationRegistration.objects.all()
    return render(request,'application_list.html',{'data':data})  


def certificate_list(request,company_name):
    data = FourWheelerParameter.objects.filter(company_name=company_name).values('model_name').distinct()
    model_names = [item['model_name'] for item in data]
    print(model_names)
    return render(request,'certificates.html',{'data':data})

        

