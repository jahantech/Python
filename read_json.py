#!/usr/bin/python


import json
from pprint import pprint

jsondata = []
with open('testdata.json') as json_file:    
	jsondata = json.load(json_file)

for Users in range(0, len(jsondata["data"])):
	print jsondata["data"][Users]["name"],jsondata["data"][Users]["age"]
