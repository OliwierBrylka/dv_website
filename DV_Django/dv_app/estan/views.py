from django.shortcuts import render, redirect
from multiprocessing import context
from django.http import HttpResponse
from django.contrib import messages
from .models import *
import os


def index(request):
    return render(request, 'index.html')

def e_stan(request):
    estan_object = estan.objects.all()
    context = { 'estan': estan_object}
    


    return render(request, 'estan.html', context)




