"""
URL configuration for projectsb project.

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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from address import views as address_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('sportsApp.urls')),
    path('match/',include('matchApp.urls')),
    path("api/",include('api.urls')),
    path('ajax/load_districts/', address_view.load_districts, name='load_districts'),
    path('ajax/load_municipalities/', address_view.load_municipalities, name='load_municipalities'),
    path('ajax/load_areas/', address_view.load_areas, name='load_areas'),
] + static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
