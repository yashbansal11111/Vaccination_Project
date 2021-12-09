from django.urls import path
from django.urls.resolvers import URLPattern
from passgenerator import views

urlpatterns = [
    path('home/',views.home, name='home'),
    path('generatedpassword/',views.password, name="password"),
]