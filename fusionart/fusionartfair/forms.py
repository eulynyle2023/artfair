
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
# from .models import Student
from django.contrib.auth.forms import PasswordResetForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.utils.translation import gettext as _

# # registration form widget
# class RegistrationForm(UserCreationForm):
#     username = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
#         required=True
#     )
#     first_name = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
#         required=True
#     )
#     last_name = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
#         required=True
#     )
#     email = forms.EmailField(
#         widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
#         required=True
#     )
#     password1 = forms.CharField(
#         widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
#         required=True
#     )
#     password2 = forms.CharField(
#         widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
#         required=True
#     )
#     date_of_birth = forms.DateField(
#         widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
#         required=True
#     )
#     address = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
#         required=True
#     )
#     city_town = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City/Town'}),
#         required=True
#     )
#     country = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country'}),
#         required=True
#     )
#     photo = forms.ImageField(
#         required=False,
#         widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'})
#     )

#     def clean_username(self):
#         username = self.cleaned_data.get("username")
#         if User.objects.filter(username=username).exists():
#             raise ValidationError("This username is already taken.")
#         return username

#     def clean_email(self):
#         email = self.cleaned_data.get("email")
#         if User.objects.filter(email=email).exists():
#             raise ValidationError("This email is already registered.")
#         return email

#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'date_of_birth', 'address', 'city_town', 'country', 'photo']
        
# class StudentProfileForm(forms.ModelForm):
#     first_name = forms.CharField(
#         max_length=255,
#         widget=forms.TextInput(attrs={'class': 'form-control'})
#     )
#     last_name = forms.CharField(
#         max_length=255,
#         widget=forms.TextInput(attrs={'class': 'form-control'})
#     )
#     email = forms.EmailField(
#         widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
#     )
#     username = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'})
#     )
#     date_of_birth = forms.DateField(
#         widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
#     )
#     address = forms.CharField(
#         max_length=255,
#         widget=forms.TextInput(attrs={'class': 'form-control'})
#     )
#     city_town = forms.CharField(
#         max_length=100,
#         widget=forms.TextInput(attrs={'class': 'form-control'})
#     )
#     country = forms.CharField(
#         max_length=100,
#         widget=forms.TextInput(attrs={'class': 'form-control'})
#     )
#     photo = forms.ImageField(
#         required=False,
#         widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
#     )

#     class Meta:
#         model = Student
#         fields = ['first_name', 'last_name', 'email', 'username', 'date_of_birth', 'address', 'city_town', 'country', 'photo']

#     def __init__(self, *args, **kwargs):
#         user = kwargs.pop('user', None)
#         super().__init__(*args, **kwargs)

#         if user:
#             self.fields['first_name'].initial = user.first_name
#             self.fields['last_name'].initial = user.last_name
#             self.fields['email'].initial = user.email
#             self.fields['username'].initial = user.username
            
            
# class CustomPasswordResetForm(PasswordResetForm):
#     def send_mail(self, subject_template_name, email_template_name, context, from_email, to_email, html_email_template_name=None):

#         html_email_content = render_to_string(email_template_name, context)
#         text_email_content = strip_tags(html_email_content)
        
#         send_mail(
#             subject=_(subject_template_name),
#             message=text_email_content,
#             html_message=html_email_content,
#             from_email=from_email,
#             recipient_list=[self.cleaned_data['email']],
#         )




class ApplyForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    sur_name = forms.CharField(max_length=100)
    ex_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    confirm_email = forms.EmailField()
    phone = forms.CharField(max_length=15)
    address = forms.CharField(widget=forms.Textarea)
    web_address = forms.URLField(required=False)
    fb_address = forms.URLField(required=False)
    insta_address = forms.URLField(required=False)
    desc_work = forms.CharField(widget=forms.Textarea)
    photoUpload1 = forms.ImageField(required=False)
    photoUpload2 = forms.ImageField(required=False)
    photoUpload3 = forms.ImageField(required=False)
    dataConsent = forms.BooleanField(required=False, initial=False)
    mailingList = forms.BooleanField(required=False, initial=False)
