from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('student_dashboard', views.student_dashboard, name='student_dashboard'),
    path('vehicle_registration', views.vehicle_registration, name='vehicle_registration'),
    path('registred_vehicle', views.registred_vehicle, name='registred_vehicle'),
    path('admin_dashboard', views.admin_dashboard, name='admin_dashboard'),
    path('pending_vehicle', views.pending_vehicle, name='pending_vehicle'),

]