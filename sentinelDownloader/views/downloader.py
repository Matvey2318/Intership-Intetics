# from sentinelDownloader.views.account import Authorization
from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt
from django.shortcuts import render, render_to_response
import json
from django.views.decorators.csrf import csrf_exempt
from collections import OrderedDict
from django.http import HttpResponse, HttpRequest
import urllib.request
import urllib.error


class DataProcessing:
    Data = dict()
    urls = []
    geojson_obj = None


user_data = DataProcessing()
api = SentinelAPI('ella_ent', '--19--09--01', 'https://scihub.copernicus.eu/dhus')


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

@csrf_exempt
def geojson_handler(request):
    if request.is_ajax() and request.method == 'POST':
        polygon_data = json.loads(request.FILES.get('polygon_data').file.read().decode('UTF-8'))
        coordinates = polygon_data.get('features')[0]['geometry']['coordinates']
        if coordinates:
            return HttpResponse('OK')
    return HttpResponse("Couldn't load data")


def find_urls(request, *geojson_obj):  # need to add conditional with geojson and footprint
    """
    Counts urls by filters

    :param request:
    JSON object with filters
    :return:
    Response with urls
    """
    user_query = get_all_data(request)
    user_data.urls.clear()
    footprint = 'POLYGON((34.322010 0.401648,36.540989 0.876987,36.884121 -0.747357,34.664474 -1.227940,34.322010 0.401648))'
    if api:
        products = api.query(footprint, **user_query)
        product_ids = list(products)
        for id in product_ids:
            user_data.urls.append(api.get_product_odata(id)['url'])
        user_data.urls = set(user_data.urls)
        user_data.urls = list(user_data.urls)
        print('OK')
        # count = str(len(user_data.urls))
    else:
        HttpResponse('False')
    return HttpResponse(json.dumps({'urls': user_data.urls}), content_type="application/json")