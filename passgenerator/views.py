from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'passgenerator/home.html')

def password(request):
    thepassword = ''
    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numerical'):
        characters.extend(list('0123456789'))
    if request.GET.get('specialchar'):
        characters.extend(list('!@#$%&*'))

    length = int(request.GET.get('length')) #because we are using length as an integer in our for loop
    for i in range(length):
        thepassword = thepassword + random.choice(characters)
    return render(request, 'passgenerator/password.html',{'password':thepassword})
