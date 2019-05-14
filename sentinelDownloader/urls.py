"""sentinelDownloader URL Configuration

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
from django.urls import path
from downloader import entrance
from django.views.generic import TemplateView
from django.conf.urls import include, url
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', TemplateView.as_view(template_name="signin.html"), name='signin'),
    path('data-table/', TemplateView.as_view(template_name="data_table.html"), name='data_table'),
    path('app/home', entrance, name='home'),
    path('', RedirectView.as_view(url='app/'))
    # path('form', views.login, name='index_two'),
    # path('download', views.download, name='download'),
    # path('home', views.get_date, name='home'),
]
