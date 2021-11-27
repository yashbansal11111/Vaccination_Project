from django.urls import path
from django.contrib.auth import views as auth_views

from . import views1,views
app_name='vaccination_drive'


urlpatterns = [
    path('login', views.loginPage, name='login'),
    path('register', views1.registerPage, name='register'),
    #path('login', auth_views.LoginView.as_view(template_name='vaccination_drive/login1.html'), name='login'), #added as test
    #path('logout', auth_views.LogoutView.as_view(template_name='vaccination_drive/logout.html'), name='logout'), #added as test
    path('addvaccine', views.VaccinationPage, name='addvaccine'),
    path('allvaccine', views.AllVaccineDetail, name='AllVaccineDetail'),
    path('allemployee', views.AllEmployeeDetail, name='AllEmployeeDetail')
]