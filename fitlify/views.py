from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # return HttpResponse('Halo')
    return render(request, 'index.html')


def home(request):
    return render(request, 'home.html')
