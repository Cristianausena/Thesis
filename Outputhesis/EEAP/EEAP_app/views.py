from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib import messages
# Create your views here.


def index(request):
    return render(request, 'html/homepage.html')

def student_dashboard(request):
    return render(request, 'html/student_dashboard.html')

def vehicle_registration(request):
    if request.method == "POST":
        plate_number = request.POST.get('plate_number')
        vehicle_model = request.POST.get('vehicle_model')
        imageF = request.POST.get('imageF')
        imageL = request.POST.get('imageL')
        imageR = request.POST.get('imageR')
        imageB = request.POST.get('imageB')
        ORCR = request.POST.get('ORCR')

        vehicle = registered_vehicles.objects.create(fname = "Sample", lname = "User", idnumber = "TUPC-19-0000", 
            platenumber = plate_number, vehiclemodel = vehicle_model, imageF = imageF, imageL = imageL, imageR = imageR,
            imageB = imageB, ORCR = ORCR)
        vehicle.save()
        messages.info(request, 'Successful Registration')
    return render(request, 'html/vehicle_registration.html')

def registred_vehicle(request):
    return render(request, 'html/registred_vehicle.html')

def admin_dashboard(request):
    return render(request, 'html/admin_dashboard.html')

def pending_vehicle(request):
    return render(request, 'html/pending_vehicle.html')

