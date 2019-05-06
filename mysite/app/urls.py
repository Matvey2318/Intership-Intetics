from django.urls import path
from . import views


urlpatterns = [
    #path('', views.get_date, name='get_date'),
    path('', views.StartPage.start, name='index'),
    path('form', views.login, name='index_two'),
    path('download', views.download, name='download'),
    #path('home', views.get_date, name='home'),
]