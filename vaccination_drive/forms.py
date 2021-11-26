from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your forms here.

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
        fields = ("name","username", "email", "password1", "password2","gender","age","contact_info","role")
    
    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.name=self.cleaned_data['name']
        user.email = self.cleaned_data['email']
        user.gender = self.cleaned_data['gender']
        user.age = self.cleaned_data['age']
        user.contact_info = self.cleaned_data['contact_info']
        user.role = self.cleaned_data['role']
        if commit:
            user.save()
        return user