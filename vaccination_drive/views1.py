from django.http import HttpResponse
from .forms import NewUserForm,VaccineAddForm,UserRegistrationForm
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from vaccination_drive.models import UserDetails, VaccinationDetails
#OR from .models import UserDetails, VaccinationDetails because our models.py is in same directory as views.py
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

def registerPage(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect("vaccination_drive:login")
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'vaccination_drive/register1.html', context)