import  pathlib
import json
from getpass import getpass
import datetime
from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt
from datetime import date
print('Sign up your uaser name')
user_name = input()
print('Sin up your password')
password = getpass('Password:')
api = SentinelAPI(user_name, password, 'https://scihub.copernicus.eu/dhus')
#api.get_product_odata('94854dc8-8c98-40e3-99b6-d067df8ada17')
#api.download('94854dc8-8c98-40e3-99b6-d067df8ada17')
footprint = geojson_to_wkt(read_geojson('../../map.geojson')) 
product = api.query(footprint,
                    date = ('NOW-7DAYS', 'NOW'),
                    #'beginposition' : datetime.date(2019,4,18
                    #endposition' : datetime.date(2019,4,25)
                    )
api.download_all(product,directory_path = 'C:/Users/Artem/Desktop',checksum = False)
