from django.core import validators
from django.db import models
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.fields.related import ForeignKey
from datetime import date

# Create your models here.


class UserDetails(models.Model):
    def __str__(self):
        return self.name
    gender_choice=(('M','Male'),('F','Female'),('Others','Others')) 
    role_choice=(('Admin','Admin'),('Employee','Employee')) 
    username=models.CharField(max_length=50,null=True)
    employee_id= models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True, null=False, blank=False)
    role = models.CharField(max_length=20,default='Employee',choices=role_choice,null=False, blank=False)
    password = models.CharField(max_length=50,null=False, blank=False)
    email_id = models.EmailField(max_length=60, unique=True, null=False, blank=False)
    gender = models.CharField(max_length=10,choices=gender_choice)
    age = models.IntegerField(validators=[MaxValueValidator(100),MinValueValidator(1)])
    contact_info = models.IntegerField(validators=[MaxValueValidator(9999999999),MinValueValidator(1000000000)])
    USERNAME_FIELD = 'username'
    

class VaccinationDetails(models.Model):
    def __str__(self):
        return self.vaccine_name
    employee=models.OneToOneField(UserDetails, on_delete=models.CASCADE,primary_key=True)
    vaccine_name=models.CharField(max_length=50,null=False, blank=False)
    first_doze = models.BooleanField()
    first_doze_date=models.DateField(validators=[MaxValueValidator(limit_value=date.today)],blank=True,null=True)
    second_doze = models.BooleanField()
    second_doze_date=models.DateField(validators=[MaxValueValidator(limit_value=date.today)],blank=True,null=True) 
#First dose date should not exceed second dose date