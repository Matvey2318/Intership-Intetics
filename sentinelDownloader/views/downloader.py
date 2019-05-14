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
            print('GOT REQUEST')
            data = dict()
            json_data = json.dumps(request.GET)
            json_data = json.loads(json_data)
            data['date'] = (json_data['beginposition'].replace('-', ''), json_data['endposition'].replace('-', ''))
            data['cloudcoverpercentage'] = (0, int(json_data['cloudcoverpercentage']))
            # data['footprint']='POLYGON ((34.322010 0.401648,36.540989 0.876987,36.884121 -0.747357,34.664474 -1.227940,34.322010 0.401648))'
            # json_data = json.loads(json_data)
            user_data.Data = OrderedDict(data)
            print(user_data.Data)
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
            user_data.urls.append(user_login.api.get_product_odata(id)['url'])
        user_data.urls = set(user_data.urls)
        user_data.urls = list(user_data.urls)
    else:
        HttpResponse('False')
    return HttpResponse(len(user_data.urls))   # need to return response


def confirmation(request):
    if request.GET:
        return render(
            request,
            'download.html',  # here will be template with urls
            context={'urls': user_data.urls}
        )
    else:
        return render_to_response(
            'index.html'
        )
