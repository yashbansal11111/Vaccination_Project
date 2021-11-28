from django.http import HttpResponse
from .forms import NewUserForm,VaccineAddForm,UserRegistrationForm
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from vaccination_drive.models import User, VaccinationDetails
#OR from .models import UserDetails, VaccinationDetails because our models.py is in same directory as views.py
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Permission

def registerPage(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            print("somethin")
            name = form.cleaned_data['name'] 
            username = form.cleaned_data['username'] 
            email = form.cleaned_data['email'] 
            password1 = form.cleaned_data['password1'] 
            gender = form.cleaned_data['gender'] 
            age = form.cleaned_data['age'] 
            contact_info = form.cleaned_data['contact_info'] 
            role = form.cleaned_data['role'] 
            print(form.__dict__)
            print(name)
            u = User(name=name,username=username,email=email,gender=gender,age=age,contact_info=contact_info,role=role,)
            u.set_password(password1)
            u.is_staff=False
            u.is_superuser=False
            u.save()
            

            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect("login")
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'vaccination_drive/register1.html', context)