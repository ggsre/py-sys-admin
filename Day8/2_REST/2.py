#!/usr/bin/env python
# 
# REST GET example 
# 
import requests

req_obj = requests.get('https://www.imdb.com/news/top?ref_=nv_tp_nw')
print(req_obj)
