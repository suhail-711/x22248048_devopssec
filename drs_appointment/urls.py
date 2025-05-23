"""
URL configuration for drs_appointment project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include
import booking.urls
import users.urls
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('signup/', include('users.urls')),
    # path('signin/', auth_views.LoginView.as_view(
    #     template_name='users/signin.html'), name='sign_in'),
    path('signout/', auth_views.LogoutView.as_view(
        template_name='users/signout.html'), name='sign_out'),
    path('admin/', admin.site.urls),
    path('',include(booking.urls)),
    # path('users/',include(users.urls)),
]
