"""
URL configuration for crashblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include

from core.views import frontpage, about, chamados, conta, estoque


urlpatterns = [
    path('admin/', admin.site.urls),
    path('chamados/', chamados, name='chamados'),
    path('conta/', conta, name='conta'),
    path('estoque/', estoque, name='estoque'),
    path('about/', about, name='about'),
    path('', include('blog.urls')),
    path('', frontpage, name='frontpage'),
]
