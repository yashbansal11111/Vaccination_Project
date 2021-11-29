from django.http import HttpResponse
from .forms import NewUserForm,VaccineAddForm,AddVaccineForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from vaccination_drive.models import User, VaccinationDetails
#OR from .models import UserDetails, VaccinationDetails because our models.py is in same directory as views.py
from django.contrib.auth import login, authenticate,logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm



# def loginPage(request):
#     if request.method == "POST":
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             #args = {'username':username,'password':password}
#             user = authenticate(username=username, password=password)
#             #user = UserDetails.objects.filter(args).values()
#             #print(user,'+++++++++++++')
#             if user is not None:
#                 login(request, user)
#                 messages.info(request, f"You are now logged in as {username}.")
#                 return redirect("vaccination_drive:addvaccine")
#             else:
#                 messages.error(request,"Invalid username or password.")
#         else:
#             messages.error(request,"Invalid username or password.")
#     form = AuthenticationForm()
#     return render(request=request, template_name="vaccination_drive/login1.html", context={"form":form})

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

def sample(request):
    if request.user.is_superuser:
        return redirect('/admin/')
    else:
        return redirect('vaccination_drive:addvaccine')


@login_required  
def VaccinationPage(request):
    user_id=request.user.id
    user_role=request.user.role
    is_admin=True if user_role=="Admin" else False
    vacc_detail=VaccinationDetails.objects.filter(employee=user_id).values()
    if not vacc_detail:
        if request.method == "POST":
            form = AddVaccineForm(request.POST)
            if form.is_valid():
                u = form.save(commit=False)
                u.employee_id = request.user.id
                u.save()
                messages.success(request, " Vaccine Registration successful." )
                return redirect("vaccination_drive:addvaccine")
            messages.error(request, "Unsuccessful Vaccine registration. Try Again.")
        form = AddVaccineForm()
        return render (request=request, template_name="vaccination_drive/vaccine_add.html", context={"form":form,"admin":is_admin})
    else:
        return render(request, "vaccination_drive/empvax_details.html", context={"empvax_details":vacc_detail,"admin":is_admin} )

@login_required
def AllVaccineDetail(request):
    vax_details=VaccinationDetails.objects.all()
    return render(request, 'vaccination_drive/vaccine_details.html', context={'vax_details':vax_details})

@login_required
def AllEmployeeDetail(request):
    emp_details=User.objects.all()
    return render(request, 'vaccination_drive/emp_details.html', context={'emp_details':emp_details})


def home(request):
    return render(request, 'vaccination_drive/home.html')
    
def logout(request):
    auth_logout(request)
    return render(request, 'vaccination_drive/logout.html')