# Generated by Django 4.1.2 on 2022-10-20 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='registered_vehicles',
            fields=[
                ('fname', models.CharField(max_length=20, verbose_name='firstname')),
                ('lname', models.CharField(max_length=20, verbose_name='lastname')),
                ('idnumber', models.CharField(max_length=12, verbose_name='idnumber')),
                ('platenumber', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True, verbose_name='platenumber')),
                ('vehiclemodel', models.CharField(max_length=12, verbose_name='vehiclemodel')),
                ('imageF', models.ImageField(upload_to='imageF/', verbose_name='frontimage')),
                ('imageL', models.ImageField(upload_to='imageL/', verbose_name='leftimage')),
                ('imageR', models.ImageField(upload_to='imageR/', verbose_name='rightmage')),
                ('imageB', models.ImageField(upload_to='imageB/', verbose_name='backmage')),
                ('ORCR', models.ImageField(upload_to='ORCR/', verbose_name='ORCR')),
                ('status', models.CharField(max_length=20, verbose_name='status')),
            ],
        ),
    ]
