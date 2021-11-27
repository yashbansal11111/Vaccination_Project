from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import date

from vaccination_drive.models import UserDetails,VaccinationDetails


# Create your forms here.

#USER REGISTRATION FORM:
class NewUserForm(UserCreationForm):
    gender_choice=(('M','Male'),('F','Female'),('Others','Others')) 
    role_choice=(('Admin','Admin'),('Employee','Employee')) 
    name = forms.CharField(max_length=50)
    email = forms.EmailField(required=True)
    gender = forms.CharField(max_length=10)
    age = forms.IntegerField(validators=[MaxValueValidator(100),MinValueValidator(1)])
    contact_info = forms.IntegerField(validators=[MaxValueValidator(9999999999),MinValueValidator(1000000000)])
    role = forms.CharField(max_length=20)
   
    class Meta:
        model = User
        fields = ["name","username","email", "password1", "password2","gender","age","contact_info","role"]
    
    def save(self, commit=True):
        User = super(NewUserForm, self).save(commit=False)
        User.name=self.cleaned_data['name']
        User.email = self.cleaned_data['email']
        User.gender = self.cleaned_data['gender']
        User.age = self.cleaned_data['age']
        User.contact_info = self.cleaned_data['contact_info']
        User.role = self.cleaned_data['role']
        if commit:
            User.save()
        return User

# VACCINATION ADD/EDIT FORM:
class VaccineAddForm(forms.ModelForm):
    class Meta:
        model = VaccinationDetails
        fields = ["vaccine_name","first_doze","first_doze_date", "second_doze", "second_doze_date"]
    
    def save(self, commit=True):
        VaccinationDetails = super(VaccineAddForm, self).save(commit=False)
        VaccinationDetails.vaccine_name=self.cleaned_data['vaccine_name']
        VaccinationDetails.first_doze = self.cleaned_data['first_doze']
        VaccinationDetails.first_doze_date = self.cleaned_data['first_doze_date']
        VaccinationDetails.second_doze = self.cleaned_data['second_doze']
        VaccinationDetails.second_doze_date = self.cleaned_data['second_doze_date']
        if commit:
            VaccinationDetails.save()
        return VaccinationDetails

# TESTING A USER REGISTRATION FORM:

class UserRegistrationForm(forms.ModelForm):
    username=forms.CharField(max_length=50)
    name = forms.CharField(max_length=50)
    email_id = forms.EmailField(required=True)
    gender = forms.CharField(max_length=10)
    age = forms.IntegerField(validators=[MaxValueValidator(100),MinValueValidator(1)])
    contact_info = forms.IntegerField(validators=[MaxValueValidator(9999999999),MinValueValidator(1000000000)])
    role = forms.CharField(max_length=20)
    password = forms.CharField(label=("Password"),widget=forms.PasswordInput)   
    password1 = forms.CharField(label=("Password confirmation"),widget=forms.PasswordInput,
    help_text=("Enter the same password as above, for verification."))    
    class Meta:
        model = UserDetails
        fields = ["name","username","email_id", "password","gender","age","contact_info","role"]


#TESTING A VACCINE ADD INFO FORM:
class AddVaccineForm(forms.ModelForm):
    vaccine_name=forms.CharField(max_length=50)
    first_doze = forms.BooleanField()
    first_doze_date=forms.DateField(validators=[MaxValueValidator(limit_value=date.today)])
    second_doze = forms.BooleanField()
    second_doze_date=forms.DateField(validators=[MaxValueValidator(limit_value=date.today)]) 
    class Meta:
        model = VaccinationDetails
        fields = ["vaccine_name","first_doze","first_doze_date", "second_doze", "second_doze_date"]