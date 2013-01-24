from django.http import HttpResponse
from django.shortcuts import render, get_list_or_404
from root.models import ServiceLevel

def index(request):
	service_levels = get_list_or_404(ServiceLevel)
	return render(request,'index.html', {'service_levels': service_levels})
	
def search(request):
	service_level = request.GET['service_level']
	weight = request.GET['weight']
	zip_code = request.GET['zip_code']
	dictionary = {'service_level': service_level, 'weight': weight, 'zip_code': zip_code}
	return render(request, 'search_result.html', dictionary)