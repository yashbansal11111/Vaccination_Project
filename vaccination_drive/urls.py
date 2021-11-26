from django.urls import path

from . import views
app_name='vaccination_drive'


urlpatterns = [
    path('login', views.loginPage, name='login'),
    path('register', views.registerPage, name='registration'),
    path('addvaccine', views.VaccinationPage, name='Vaccination Page'),
    path('allvaccine', views.AllVaccineDetail, name='AllVaccineDetail'),
    path('allemployee', views.AllEmployeeDetail, name='AllEmployeeDetail')
]