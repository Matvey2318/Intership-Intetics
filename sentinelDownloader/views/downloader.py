from sentinelDownloader.views.account import Authorization
from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt
from django.shortcuts import render, render_to_response
import json
from collections import OrderedDict
from django.http import HttpResponse, HttpRequest
import urllib.request
import urllib.error


class DataProcessing:
    Data = dict()
    urls = []
    geojson_obj = None


user_login = Authorization()  #user's instance of LogIn
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


def entrance(request):  # runs on index.html
    connect(request)

    """
    returns form with map and forms
    """
    return render(
        request,
        'index.html',
        context={}
    )


def get_all_data(request): #geojson_obj):
    if request.is_ajax():
        if request.method == 'GET':
            json_data = json.load(request.GET)  # loads
            user_data.Data = OrderedDict(json_data)
    return user_data.Data


def geojson_handler(request):
    print('GOT IN')
    if request.is_ajax():
        if request.method == 'POST':
            user_data.geojson_obj = request.FILES['geojson']

    return HttpResponse('OK')


def find_urls(request, *geojson_obj):  # need to add conditional with geojson and footprint
    """
    Counts urls by filters

    :param request:
    JSON object with filters
    :return:
    amount of urls
    """
    user_query = get_all_data(request)
    user_data.urls.clear()
    if user_login.api:
        products = user_login.api.query(**user_query)
        product_ids = list(products)
        for id in product_ids:
            user_data.urls.append(user_login.api.get_product_odatjhea(id)['url'])
        user_data.urls = set(user_data.urls)
        user_data.urls = list(user_data.urls)
    else:
        HttpResponse('False')
    return len(user_data.urls)   # need to return response


def confirmation(request):
    if request.GET:
        return render(
            request,
            'download.html',
            context={'urls': user_data.urls}
        )
    else:
        return render_to_response(
            'index.html'
        )
