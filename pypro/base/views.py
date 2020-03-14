from django.http import HttpResponse
<<<<<<< HEAD
=======
from django.shortcuts import render
>>>>>>> origin/3

# Create your views here.


def home(request):
    return HttpResponse('Olá Django!')
