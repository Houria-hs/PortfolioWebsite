from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import project , testimonial
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
# Create your views here.

def home (request):
    projects = project.objects.all()
    testimonials = testimonial.objects.all()
    return render(request, 'home.html' , {'projects': projects , 'testimonials':testimonials})

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get("name_inp")
        email = request.POST.get("email_inp")
        phone = request.POST.get("number_inp")
        budget = request.POST.get("budget_inp")
        message = request.POST.get("message_inp")

        full_message = f"""
        New contact form submission:
        Name: {name}
        Email: {email}
        Phone: {phone}
        Budget: {budget}
        Message: {message}
        """
        send_mail(
            subject=f"Visionpulse Contact from {name}",
            message=full_message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=["houriahasbell@gmail.com"], 
            fail_silently=False,
        )

        messages.success(request, "Your message has been sent successfully!")
        return redirect('contact')  
    return render(request, "home.html")