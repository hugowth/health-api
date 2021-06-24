"""health_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path, include

from health_api import views

from drf_spectacular.views import (
    SpectacularJSONAPIView,
    SpectacularRedocView,
)


public_patterns = (
    [path('', include('core.urls'))],
    'public',
)


urlpatterns = [
    path('', views.version, name='index'),
    path('', include(public_patterns)),
    path(
        'schema/',
        SpectacularJSONAPIView.as_view(api_version='v1'),
        name='schema',
    ),
    path(
        'redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc',
    ),
]
