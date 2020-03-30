# -*- coding: utf-8 -*-
import json
from urllib.request import urlopen, quote
import requests,csv
import pandas as pd
import urllib.parse
import urllib

def getlnglat(address):
    url = 'https://api.map.baidu.com/geocoding/v3/'
    output = 'json'
    ak = 'oOnDS3y3z9Hi4K3KXc2GmotPHXgQUfou'
    add = quote(address)
    s = '请求'
    s = urllib.parse.quote(s)
    uri = url + '?' + 'address=' + add  + '&output=' + output + '&ak=' + ak
    req = urlopen(uri)
    res = req.read().decode()
    temp = json.loads(res)
    return temp

file = open(r'D:\PYTHON\求职之路\point.json','w',encoding='utf-8')
with open(r'D:\PYTHON\求职之路\new_51job_2.csv', 'r',encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        if reader.line_num == 1:
            continue
        b = line[0]
        c= line[1]
        lng = getlnglat(b)['result']['location']['lng']
        lat = getlnglat(b)['result']['location']['lat']
        str_temp = '{"lat":' + str(lat) + ',"lng":' + str(lng) + ',"count":' + str(c) +'},'
        print(str_temp)
        file.write(str_temp)
file.close()

