# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt
from django.shortcuts import render, render_to_response
from django.shortcuts import redirect
import datetime
from django.utils import timezone
from collections import OrderedDict
from django.http import HttpResponse, HttpRequest
from django import forms
import urllib.request
from download import check_count, downloader


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


class DataProcessing:
    Data = dict()
    urls = []


user_login = Authorization()  # user's instance of LogIn
user_data = DataProcessing()


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
    def start(self):  # need to use TemplateView
        return render(
            None,
            'index.html'

        )


def entrance(request):  #runs on index.html
    connect(request)

    """
    returns form with map and forms
    """
    return render(
        request,
        'test_form.html',
        context={}
    )


def get_all_data(request):  # geojson_obj):
    if request.is_ajax():
        if request.method == 'GET':
            json_data = json.load(request.GET)  # loads
            user_data.Data = OrderedDict(json_data)
    return user_data.Data






