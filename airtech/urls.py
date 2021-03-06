"""airtech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from airtech.views import IndexAPIView

urlpatterns = [
    path('', IndexAPIView.as_view(), name='index'),
    path('api/v1/auth/', include('airtech.apps.authentication.urls',
                                 namespace='authentication')),
    path('api/v1/', include('airtech.apps.flights.urls',
                            namespace='flights')),
    path('api/v1/flights/', include('airtech.apps.tickets.urls',
                                    namespace='tickets')),
    path('admin/', admin.site.urls),
]
