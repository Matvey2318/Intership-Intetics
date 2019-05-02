from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_date, name='get_date'),
    path('index.html', views.result, name='index'),
    path('home', views.get_date, name='home'),
]