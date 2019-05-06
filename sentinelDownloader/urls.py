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
from downloader import StartPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', StartPage.start, name='index'),
    # path('', views.get_date, name='get_date'),
    # path('form', views.login, name='index_two'),
    # path('download', views.download, name='download'),
    # path('home', views.get_date, name='home'),
]
