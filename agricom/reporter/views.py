from django.shortcuts import render

from django.views.generic import TemplateView
from django.http import HttpResponse
from .models import County,Incidence


# Create your views here.

class HomePageView(TemplateView):
    template_name = 'index.html'
