from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import project , testimonial
# Create your views here.

def home (request):
    projects = project.objects.all()
    testimonials = testimonial.objects.all()
    return render(request, 'home.html' , {'projects': projects , 'testimonials':testimonials})