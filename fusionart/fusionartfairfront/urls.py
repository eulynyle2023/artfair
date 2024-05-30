"""
URL configuration for registrationapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from fusionartfair import views
from django.conf import settings
from django.conf.urls.static import static
# from registration.views import LoginApi
# from registration.views import register_module, unregister_module, my_registered_modules
from django.contrib.auth import views as auth_views
# from registration.forms import CustomPasswordResetForm


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about_us, name='about_us'),
    path('contact/', views.contact_us, name='contact_us'),
    path('visit/', views.visit, name='visit'),
    # path('courses/<int:course_id>/', views.course_detail, name='course_detail'),
    path('apply/', views.apply, name='apply'),
    path('terms/', views.terms, name='terms'),
    path('privacy/', views.privacy, name='privacy'),
    # path('login/', views.user_login, name='login'),
    # path('register/', views.register, name='register'),
    # path('modules/<str:code>/', views.module_detail, name='module_detail'), 
    # path('profile/', views.profile, name='profile'),
    # path('logout/', views.logout_view, name='logout'),
    # path('modules/<str:code>/register/', views.register_module, name='register_module'),
    # path('modules/<str:code>/unregister/', views.unregister_module, name='unregister_module'),
    # path('profile/edit/', views.edit_profile, name='edit_profile'),
    # path('password_reset/', auth_views.PasswordResetView.as_view(form_class=CustomPasswordResetForm), name='password_reset'),
    # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    # path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    # path('profile/my_modules', my_registered_modules, name='my_modules'),
    
    # # API
    # path("auth/login/", LoginApi.as_view(), name="api_login"),
    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)