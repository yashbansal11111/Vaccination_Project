#To make the application modifiable in browser
from django.contrib import admin

# Register your models here.
from .models import User, VaccinationDetails

class UserAdmin(admin.ModelAdmin):
    list_display=('username','age','role')
    ordering=('username',)
admin.site.register(User,UserAdmin)
admin.site.register(VaccinationDetails) 



#Both registrations should be done seperately !!
