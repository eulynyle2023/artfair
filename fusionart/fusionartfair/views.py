from django.shortcuts import render, get_object_or_404, redirect
# from .models import Module, Course, Student, Registration
from .forms import  ApplyForm
from django.contrib import messages
# from django.db.models import Q
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
from functools import wraps
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import EmailMessage


def home(request):

    return render(request, 'fusionartfair/home.html')

# about us page of the website
def about_us(request):

    return render(request, 'fusionartfair/about_us.html')


def visit(request):
   
    return render(request, 'fusionartfair/visit.html')

def terms(request):
 
    return render(request, 'fusionartfair/terms.html')


def privacy(request):
 
    return render(request, 'fusionartfair/privacy.html')


def contact_us(request):
    if request.method == 'POST':
        
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        
        email_subject = f"New Contact Form Submission: {subject}"
        email_context = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message,
        }
        
        # Send an email
        send_mail(
            subject = email_subject,
            message = message,

            from_email=settings.EMAIL_HOST_USER,
            to=['info@fusionartfair.co.uk'],
            fail_silently = False,
        )
        
        messages.success(request, "Your message has been sent. We'll get back to you soon!")
        return redirect('contact_us')

    return render(request, 'fusionartfair/contact_us.html')




def apply(request):
    if request.method == 'POST':
        form = ApplyForm(request.POST, request.FILES)
        print(form.data)
        if form.is_valid():
            # Extract form data
            print('Im here')
            first_name = form.cleaned_data['first_name']
            sur_name = form.cleaned_data['sur_name']
            ex_name = form.cleaned_data['ex_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            address = form.cleaned_data['address']
            web_address = form.cleaned_data['web_address']
            fb_address = form.cleaned_data['fb_address']
            insta_address = form.cleaned_data['insta_address']
            desc_work = form.cleaned_data['desc_work']
            data_consent = form.cleaned_data.get('dataConsent', False)
            add_to_mailing_list = form.cleaned_data.get('mailingList', False)  # Get the optional checkbox value

            # Create email message
            subject = "New Application Form Exhibition"
            message = f"""Please find the details of a new application to exhibit:
            FirstName: {first_name}
            Surname: {sur_name}
            ExhibitorName: {ex_name}
            Email: {email}
            Phone: {phone}
            Address: {address}
            Website: {web_address}
            Facebook: {fb_address}
            Instagram: {insta_address}
            DescriptionofWork: {desc_work}
            DataConsent: {data_consent}
            AddToMailingList: {add_to_mailing_list}
            """
            print(settings.EMAIL_HOST_USER)
            # Create EmailMessage instance
            email_message  = EmailMessage(
                subject=subject,
                body=message,
                from_email=settings.EMAIL_HOST_USER,
                to=['info@fusionartfair.co.uk']  # Change to your recipient email
            )
            # Attach images if provided
            if 'photoUpload1' in request.FILES:
                photo_upload1 = request.FILES['photoUpload1']
                email_message.attach(photo_upload1.name, photo_upload1.read(), photo_upload1.content_type)
            if 'photoUpload2' in request.FILES:
                photo_upload2 = request.FILES['photoUpload2']
                email_message.attach(photo_upload2.name, photo_upload2.read(), photo_upload2.content_type)
            if 'photoUpload3' in request.FILES:
                photo_upload3 = request.FILES['photoUpload3']
                email_message.attach(photo_upload3.name, photo_upload3.read(), photo_upload3.content_type)

           
            res = email_message.send()
            print(res)

            messages.success(request, "Your message has been sent. We'll get back to you soon!")
            return redirect('apply')

    else:
        form = ApplyForm()

    return render(request, 'fusionartfair/apply.html', {'form': form})

