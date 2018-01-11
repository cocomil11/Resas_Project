# -*- coding: utf-8 -*-
import json
import pandas as pd
from pandas.io.json import json_normalize
import unicodecsv as csv
#超重要！！上をシステムが使ってるCSVじゃなくて、このようにすることでCSVに書き込みのときのUnicodeエラーを防げる！！import requests
api_key = 'JT8xGoXj90mJDwrYvU6cax4oPYUfavLl4KVBCTLo'
url ="https://opendata.resas-portal.go.jp/"
headers = {
            'Content-Type': 'application/json',
            'X-API-KEY':api_key
            }

def resas_api_pref_request():
    url_to_data = 'api/v1-rc.1/prefectures'
    data =  requests.get(url=url+url_to_data,headers=headers)
    return  data

def resas_api_tourism_attraction_request(prefCode, cityCode):
    url_to_data = 'api/v1/tourism/attractions'
    params = {'prefCode':prefCode,'cityCode':cityCode}
    data =  requests.get(url=url+url_to_data,headers=headers,params=params)
    return  data

def resas_api_city_request():
    url_to_data = 'api/v1/cities'
    data =  requests.get(url=url+url_to_data,headers=headers)
    return  data

def resas_api_broad_industry_request():
    url_to_data = 'api/v1/industries/broad'
    data =  requests.get(url=url+url_to_data,headers=headers)
    return  data

def resas_api_middle_industry_request():
    url_to_data = 'api/v1/industries/middle'
    data =  requests.get(url=url+url_to_data,headers=headers)
    return  data

def resas_api_narrow_industry_request():
    url_to_data = 'api/v1/jobs/broad'
    data =  requests.get(url=url+url_to_data,headers=headers)
    return  data

def resas_api_broad_jobs_request():
    url_to_data = 'api/v1/industries/narrow'
    data =  requests.get(url=url+url_to_data,headers=headers)
    return  data

def resas_api_middle_jobs_request():
    url_to_data = 'api/v1/jobs/middle'
    data =  requests.get(url=url+url_to_data,headers=headers)
    return  data

def resas_api_empedu_request(prefId, displayMethod, matter, classification, displayType, gender):
    url_to_data = 'api/v1/employEducation/localjobAcademic/toTransition'
    params = {'prefecture_cd':prefId,'displayMethod':displayMethod,'matter':matter,'classification':classification,'displayType':displayType,'gender':gender}
    data =  requests.get(url=url+url_to_data,headers=headers,params=params)
    return  data
# https://opendata.resas-portal.go.jp/docs/api/v1/employEducation/localjobAcademic/toTransition.html

def resas_api_patents_broad_request():
    url_to_data= 'api/v1/patents/broad'
    data =  requests.get(url=url+url_to_data,headers=headers)
    return  data

def resas_api_estimate_request(prefCode, cityCode, addArea=None):
    url_to_data = 'api/v1/population/sum/estimate'
    params = {'prefCode':prefCode, 'cityCode':cityCode, 'addArea':addArea}
    data = requests.get(url=url+url_to_data, headers=headers, params=params)
    return data

def resas_api_labor2012_request(prefCode, cityCode, sicCode, simcCode, year='2012'):
    url_to_data = 'api/v1/municipality/labor/perYear'
    params = {'year':year, 'prefCode':prefCode, 'cityCode':cityCode, 'sicCode':sicCode, 'simcCode':simcCode}
    data = requests.get(url=url+url_to_data, headers=headers, params=params)
    return data

'''
data = resas_api_broad_industry_request()._content.decode('UTF-8')
x = json.loads(data)
broadIn = pd.DataFrame.from_dict(x['result'])
#print broadIn

data = resas_api_middle_industry_request()._content.decode('UTF-8')
x = json.loads(data)
middleIn = pd.DataFrame.from_dict(x['result'])
#print middleIn


data = resas_api_broad_jobs_request()._content.decode('UTF-8')
x = json.loads(data)
broadJobs = pd.DataFrame.from_dict(x['result'])
#print broadJobs


data = resas_api_middle_jobs_request()._content.decode('UTF-8')
x = json.loads(data)
middleJobs = pd.DataFrame.from_dict(x['result'])
#print middleJobs


data = resas_api_labor2012_request('47','-','-','-')._content.decode('UTF-8')
x = json.loads(data)
labor2012 = json_normalize(x['result'],'data',['sicName','cityCode','prefCode','cityName','prefName','simcName'])
#print labor2012


data = resas_api_patents_broad_request()._content.decode('UTF-8')
x = json.loads(data)
#json to dict
patents = pd.DataFrame.from_dict(x['result'])
#print patents


data = resas_api_city_request()._content.decode('UTF-8')
x = json.loads(data)
cities = pd.DataFrame.from_dict(x['result'])
#print cities


data = resas_api_pref_request()._content.decode('UTF-8')
x = json.loads(data)
pref = pd.DataFrame.from_dict(x['result'])
#print pref


data = resas_api_empedu_request('47','0','0','0','00','0')._content.decode('UTF-8')
x = json.loads(data)
empedu = json_normalize(x['result']['changes'],'data',['prefCode', 'label'])#a bit difficult // .json_normalize
#print empedu


data = resas_api_estimate_request('47','-')._content.decode('UTF-8')
x = json.loads(data)
estimate = json_normalize(x['result']['data'],'data','label')
boundaryYear = x['result']['boundaryYear']
estimate['boundaryYear']=boundaryYear
#print estimate
'''

