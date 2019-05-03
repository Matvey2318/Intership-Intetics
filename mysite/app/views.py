# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt
from django.shortcuts import render, render_to_response
from django.shortcuts import redirect
import datetime
from django.utils import timezone
from collections import OrderedDict
from django.http import HttpResponse, HttpRequest
#from .forms import Cloudcoverpercentage
#from .models import Book, Author, BookInstance, Genre
from django import forms
import urllib.request


class Authorization:
    """
    includes:
    - getting login and psswd
    - api
    """
    Login_data = dict()
    api = None

    def login(self, request):
        if 'login' in request.GET:
            self.Login_data['login'] = request.GET['login']
        else:
            return HttpResponse('No login in your form')
        if 'password' in request.GET:
            self.Login_data['password'] = request.GET['password']
            return
        else:
            return HttpResponse('No password in your form')


user_login = Authorization()  #user's instance of LogIn


def connect(request):
    """
    connecting to API
    """
    user_login.login(request)
    try:
        user_login.api = SentinelAPI(user_login.Login_data['login'], user_login.Login_data['password'],
                                         'https://scihub.copernicus.eu/dhus')
    except urllib.error.HTTPError as err:
        if err.code == 403:
            HttpResponse('Wrong login or password')
    return


class StartPage:
    def start(self):
        return render(
            None,
            'index.html'

        )


def start_second(request):  #runs on index.html
    connect(request)

    """
    returns form with map and forms
    """
    return render(
        request,
        'test_form.html',
        context={}
    )


class Getdata():
    Data = dict()

def get_cloudcoverpercentage(request, dict_data):
     if 'cloud_lower' in request.GET and 'cloud_upper' in request.GET:
        dict_data['cloudcoverpercentage'] = (request.GET['cloud_lower'], request.GET['cloud_upper'])
        return
     else:
        return

def get_date(request, dict_data):
    if 'date_lower' in request.GET and 'date_upper' in request.GET:
        print(request.GET['date_lower'], request.GET['date_upper'], type(request.GET['date_lower']), type(request.GET['date_upper']))
        if request.GET['date_lower'] < request.GET['date_upper']:
            dict_data['date'] = (request.GET['date_lower'].replace('-', ''), request.GET['date_upper'].replace('-', ''))
        elif request.GET['date_lower'] == request.GET['date_upper']:
            dict_data['date'] = request.GET['date_lower'].replace('-', '')
    else:
        dict_data['date'] = 'NOW'   #default
    return

def get_footprint(request, geojson_obj, dict_data):
    if True:  #need a condition
        dict_data['footprint'] = geojson_to_wkt(geojson_obj)
    return


def get_all_data(request): #geojson_obj):
    user_data = Getdata()
    get_cloudcoverpercentage(request, user_data.Data)
    #get_date(request, user_data.Data)
    #self.get_footprint(request, geojson_obj) - gets footprint, no need now
    user_data.Data = OrderedDict(user_data.Data)
    return user_data.Data


class DataProcessing():
    urls = []


def download(request):  #geojson_obj):
    user_query = get_all_data(request)
    #api = SentinelAPI(user_login['login'], user_login['p
    if user_login.api:
        products = user_login.api.query(**user_query)
    else:
        HttpResponse('False')
    #downloading is here
    #api.download_all(products)
    product_ids = list(products)
    print(product_ids)
    user_urls = DataProcessing
    for id in product_ids:
        user_urls.urls.append(user_login.api.get_product_odata(id)['url'])
    print('OK')
    print(user_urls.urls[0])
    return render(
         request,
         'download.html',
         context={'urls': user_urls.urls}
    )

