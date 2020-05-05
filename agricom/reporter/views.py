from django.shortcuts import render

from django.views.generic import TemplateView
from django.http import HttpResponse
from .models import County,Incidence
from django.core.serializers import serialize


# Create your views here.

class HomePageView(TemplateView):
    template_name = 'index.html'

def IncidenceData(request):
    points= serialize('geojson', Incidence.objects.all())
    return HttpResponse(points,content_type='json')
def CountyData(request):
    counties = serialize('geojson', County.objects.all())
    return HttpResponse(counties,content_type='json')   