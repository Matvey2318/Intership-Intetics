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
#api = SentinelAPI('ella_ent', '--19--09--01', 'https://scihub.copernicus.eu/dhus')



class LogIn:
    Login_data = dict()

    def login(self, request):
        if 'login' in request.GET:
            self.Login_data['login'] = request.GET['login']
            return
        else:
            return HttpResponse('No login in your form')

    def password(self, request):
        if 'password' in request.GET:
            self.Login_data['password'] = request.GET['password']
            return
        else:
            return HttpResponse('No password in your form')

    def connect(self, request):
        self.login(request)
        self.password()
        try:
            api = SentinelAPI(self.Login_data['login'], self.Login_data['password'], 'https://scihub.copernicus.eu/dhus')
        except urllib.error.HTTPError as err:
            if err.code == 403:
                HttpResponse('Wrong login or password')
        return


class Authorization:
    user_login = LogIn()

    def start(self):
        return render(
            HttpRequest.scheme,
            'index.html'
        )

    def start_second(self, request):  #run on index.html
        user_login.connect(request)
        """
        returns form with map and forms
        """
        return render(
            request,
            'index.html',
            context={}
        )


class Getdata(LogIn):
    Data = dict()

    def get_cloudcoverpercentage(self, request):
        if 'cloud_lower' in request.GET and 'cloud_upper' in request.GET:
            self.Data['cloudcoverpercentage'] = (request.GET['cloud_lower'], request.GET['cloud_upper'])
            return
        else:
            return

    def get_date(self, request):
        if 'date_lower' in request.GET and 'date_upper' in request.GET:
            if request.GET['date_lower'] < request.GET['date_upper']:
                self.Data['date'] = (request.GET['date_lower'], request.GET['date_upper'])
            elif equest.GET['date_lower'] == request.GET['date_upper']:
                self.Data['date'] = request.GET['date_lower']
            else:
                self.Data['date'] = 'NOW'   #default
        return

    def get_footprint(self, request, geojson_obj):
        if True:  #need a condition
            self.Data['footprint'] = geojson_to_wkt(geojson_obj)
        return

    def get_all_data(self, request, geojson_obj):
        self.get_cloudcoverpercentage(request)
        self.get_date(request)
        self.get_footprint(request, geojson_obj)
        self.Data = OrderedDict(self.Data)


class DataProcessing(LogIn):

    def download(request, geojson_obj):
        Getdata.get_all_data(request, geojson_obj)
        products = api.query(**Getdata.Data)
        #downloading is here
        #api.download_all(products)
        product_ids = list(products)
        return render_to_response(
            request,
            'index.html',
            context={'product_ids': product_ids}
        )

