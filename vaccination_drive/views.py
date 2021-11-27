from django.http import HttpResponse
from .forms import NewUserForm,VaccineAddForm,AddVaccineForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from vaccination_drive.models import UserDetails, VaccinationDetails
#OR from .models import UserDetails, VaccinationDetails because our models.py is in same directory as views.py
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

def loginPage(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            #args = {'username':username,'password':password}
            user = authenticate(username=username, password=password)
            #user = UserDetails.objects.filter(args).values()
            print(user,'+++++++++++++')
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("vaccination_drive:addvaccine")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="vaccination_drive/login1.html", context={"form":form})

# def registerPage(request):
#     if request.method == "POST":
#         form = NewUserForm(request.POST)
#         if form.is_valid():
#             User = form.save()
#             login(request, User)
#             messages.success(request, "Registration successful." )
#             return redirect("vaccination_drive:login")
#         messages.error(request, "Unsuccessful registration. Invalid information.")
#     form = NewUserForm()
#     return render (request=request, template_name="vaccination_drive/register1.html", context={"form":form})
   
def VaccinationPage(request):
    if request.method == "POST":
        form = AddVaccineForm(request.POST)
        if form.is_valid():
            User = form.save()
            login(request, User)
            messages.success(request, " Vaccine Registration successful." )
            #return redirect("vaccination_drive:login")
        messages.error(request, "Unsuccessful Vaccine registration. Try Again.")
    form = AddVaccineForm()
    return render (request=request, template_name="vaccination_drive/vaccine_add.html", context={"form":form})
   

def AllVaccineDetail(request):
    vax_details=VaccinationDetails.objects.all()
    return render(request, 'vaccination_drive/vaccine_details.html', context={'vax_details':vax_details})

def AllEmployeeDetail(request):
    emp_details=UserDetails.objects.all()
    return render(request, 'vaccination_drive/emp_details.html', context={'emp_details':emp_details})