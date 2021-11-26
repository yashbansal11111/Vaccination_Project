#To make the application modifiable in browser
from django.contrib import admin

# Register your models here.
from .models import UserDetails, VaccinationDetails

admin.site.register(UserDetails)
admin.site.register(VaccinationDetails) 

#Both registrations should be done seperately !!
