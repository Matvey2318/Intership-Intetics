from account import Authorization
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
    product_ids = []


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


def entrance(request):  # runs on signin.html
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


def check_count(request, *geojson_obj):
    """
    Counts products by filters
    :param request:
    JSON object with filters
    :return:
    amount of urls
    """
    user_query = get_all_data(request)
    user_data.product_ids.clear()
    if user_login.api:
        if geojson_obj:
            footprint = geojson_to_wkt(read_geojson(geojson_obj))
            # Artem has to check that request always contains footprint (in JSON) or geojson_obj
            products = user_login.api.query(footprint, **user_query)
        else:
            products = user_login.api.query(**user_query)
        user_data.product_ids = list(products)
        user_data.product_ids = set(user_data.product_ids)
        user_data.product_ids = list(user_data.product_ids)
    else:
        HttpResponse('False')
    return HttpResponse(json.dumps(len(user_data.product_ids)), mimetype='application/json')   # ? - not use json, just len


def confirmation(request):
    """
    Makes a response with filtered data
    :param request:
    Boolean (True if action is confirmed)
    :return:
    JSON with id and url of each queried product
    """
    user_data.urls.clear()
    if request.GET:
        response_urls = dict()
        for id in user_data.product_ids:
            response_urls[id] = user_login.api.get_product_odatjhea(id)['url']
            user_data.urls.append(response_urls[id])
        return HttpResponse(json.dumps(response_urls), mimetype='application/json')
    else:
        return render_to_response(
            'index.html'
        )  # need response?