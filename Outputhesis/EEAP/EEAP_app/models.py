from email.policy import default
from tabnanny import verbose
from django.db import models

# Create your models here.

class registered_vehicles(models.Model):
    fname = models.CharField(max_length = 20, verbose_name = 'firstname')
    lname = models.CharField(max_length = 20, verbose_name = 'lastname')
    idnumber = models.CharField(max_length = 12, verbose_name = 'idnumber')
    platenumber = models.CharField(primary_key = True, unique = True , max_length = 10, verbose_name = 'platenumber')
    vehiclemodel = models.CharField(max_length = 12, verbose_name = 'vehiclemodel')
    imageF = models.ImageField(upload_to = "imageF/", verbose_name = 'frontimage')
    imageL = models.ImageField(upload_to = "imageL/", verbose_name = 'leftimage')
    imageR = models.ImageField(upload_to = "imageR/", verbose_name = 'rightmage')
    imageB = models.ImageField(upload_to = "imageB/", verbose_name = 'backmage')
    ORCR = models.ImageField(upload_to = "ORCR/", verbose_name = 'ORCR')
    status = models.CharField(max_length = 20, verbose_name = 'status')
    

