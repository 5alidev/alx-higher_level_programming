#!/usr/bin/python3
'''args to json file'''
import sys
import json
import os.path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

jsonList = []
if os.path.exists("add_item.json"):
    jsonList = load_from_json_file("add_item.json")

for arg in sys.argv[1:]:
    jsonList.append(arg)

save_to_json_file(jsonList, "add_item.json")
