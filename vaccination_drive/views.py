from django.http import HttpResponse
from .forms import NewUserForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from vaccination_drive.models import UserDetails, VaccinationDetails


def loginPage(request):
    loginfo=UserDetails.objects.all().values_list('employee_id','password')
    return HttpResponse(loginfo)

def registerPage(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("vaccination_drive:login")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request=request, template_name="vaccination_drive/register.html", context={"register_form":form})
   
def VaccinationPage(request):
    vax_reg=VaccinationDetails.objects.all().values_list()
    return HttpResponse(vax_reg)

def AllVaccineDetail(request):
    vax_details=VaccinationDetails.objects.all().values()
    outputvax =[q for q in vax_details]
    print(type(vax_details))
    return HttpResponse(outputvax)

def AllEmployeeDetail(request):
    all_details=UserDetails.objects.all().values()
    return HttpResponse(all_details)