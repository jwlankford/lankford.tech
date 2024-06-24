from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
import requests
import datetime

# Create your views here.
def home(request):
    return render(request, 'home.html')