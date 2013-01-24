from django.http import HttpResponse
from django.shortcuts import render, get_list_or_404, get_object_or_404
from root.models import ServiceLevel, Zone

def index(request):
    service_levels = get_list_or_404(ServiceLevel)
    return render(request, 'index.html', {'service_levels': service_levels})


def search(request):
    service_level = request.GET['service_level']
    weight = request.GET['weight']
    zip_code = request.GET['zip_code']
    zone = get_object_or_404(Zone, service_level=service_level, zip_code=zip_code)
    return render(request, 'search_result.html', {'zone': zone})