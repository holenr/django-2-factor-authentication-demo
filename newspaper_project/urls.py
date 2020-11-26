# newspaper_project/urls.py
"""newspaper_project URL Configuration

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
from django.urls import path, include #new ch 9
from django.views.generic.base import TemplateView # new ch 9

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')), # new ch 9 (our own users app, for urls/ views for 'signup' page)
    path('users/', include('django.contrib.auth.urls')), # new ch 9 (the django built-in auth app, contains urls/ views for login and logout...)
    path('', TemplateView.as_view(template_name='home.html'), name='home'), # new ch 9 (TemplateVie allows us to set a template_name right in the URL pattern, preventing us from having to create a dedicated "pages" app just yet)
]
