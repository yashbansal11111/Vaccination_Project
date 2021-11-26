# Generated by Django 4.1.dev20211124163835 on 2021-11-26 06:52

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaccination_drive', '0002_remove_vaccinationdetails_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='contact_info',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(9999999999), django.core.validators.MinValueValidator(1000000000)]),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('Others', 'Others')], max_length=10),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='role',
            field=models.CharField(choices=[('Admin', 'Admin'), ('Employee', 'Employee')], default='Employee', max_length=20),
        ),
        migrations.AlterField(
            model_name='vaccinationdetails',
            name='first_doze_date',
            field=models.DateField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(limit_value=datetime.date.today)]),
        ),
        migrations.AlterField(
            model_name='vaccinationdetails',
            name='second_doze_date',
            field=models.DateField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(limit_value=datetime.date.today)]),
        ),
    ]
