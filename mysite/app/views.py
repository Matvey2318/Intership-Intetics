# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt
from django.shortcuts import render, render_to_response
from django.shortcuts import redirect
import datetime
from django.utils import timezone
from collections import OrderedDict
from django.http import HttpResponse
#from .forms import Cloudcoverpercentage
#from .models import Book, Author, BookInstance, Genre
from django import forms

api = SentinelAPI('ella_ent', '--19--09--01', 'https://scihub.copernicus.eu/dhus')


class Cloudcoverpercentage(forms.Form):
    lower_bound = forms.FloatField()
    upper_bound = forms.FloatField()


def get_date(request):
    return render(
        request,
        'test_form.html',
        context={'form': Cloudcoverpercentage(request.GET)},
    )

#def index(request):
#    return render(
#        request,
#        'index.html',
#        context={},
#    )


def result(request):
    form = Cloudcoverpercentage(request.GET)
    if form.is_valid():
        products = {'cloudcoverpercentage': (form.cleaned_data['lower_bound'], form.cleaned_data['upper_bound'])}
        q = api.query(**products)
        download = api.download_all(q)
        return render_to_response(
            request,
            'index.html',
            context={'download': download}
        )
    else:
        return HttpResponse('False')

#    else:
#        return HttpResponse('Please submit a search term.')