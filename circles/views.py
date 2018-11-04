from django.shortcuts import render
from django.http import HttpResponse, Http404

def circles(request):
	context = {}
	return render(request, 'circles/circles.html', context)