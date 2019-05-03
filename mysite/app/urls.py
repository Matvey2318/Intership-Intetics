from django.urls import path
from . import views


urlpatterns = [
    #path('', views.get_date, name='get_date'),
    path('', views.Authorization.start(request), name='index'),
    path('form', views.Authorization.start_second, name='index_two'),
    #path('home', views.get_date, name='home'),
]