#!/usr/bin/env python
# 
# REST POST example 
# 
import requests
import json

url_name = 'http://httpbin.org/post'
data = {"Name" : "John"}
data_json = json.dumps(data)
headers = {'Content-type': 'application/json'}
response = requests.post(url_name, data=data_json, headers=headers)
print(response)
