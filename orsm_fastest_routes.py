# -*- coding: utf-8 -*-
import json
import requests
api_key = '58d904a497c67e00015b45fc102989de018648854f13843da0698fb1'
url ="https://api.openrouteservice.org/"
headers = {
            'Content-Type': 'application/json',
            'Authorization':api_key
            }
            ##大問題だった！！この上！！'X-API-KEY'では上手く行かないことがあるみたい、、なんでかわからん！！
params = {'coordinates':'8.34234,48.23424 | 8.34423,48.26424', 'profile':'driving-hgv'}

def get_direction(coordinates,profile,):
    url_to_data = 'directions'
    params = {'coordinates':coordinates, 'profile':profile, 'preference':'fastest','units':'m','language':'en'}
    data =  requests.get(url=url+url_to_data,headers=headers,params=params)
    return  data

x = json.loads(get_direction(*params)._content.decode('UTF-8'))
print x['routes'][0]

