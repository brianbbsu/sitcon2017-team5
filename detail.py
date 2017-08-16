import requests
import json
import urllib
from bot import read
from pprint import pprint

base="https://maps.googleapis.com/maps/api/place/details/json?key=AIzaSyBeqKyY86QL_Ao23mEyDUGFuj7bjyag2Og&placeid="

def get_detail(pid):
	raw=requests.get(base+str(pid))
	js=json.loads(raw.text)
	#pprint(js)
	print(base+str(pid))
	
	rt={}

	if "formatted_address" in js["result"]:
		rt["add"]=js["result"]["formatted_address"]
	else:
		rt["add"]="N/A"

		
	if "formatted_phone_number" in js["result"]:
		rt["tel"]=str(js["result"]["formatted_phone_number"])
	else:
		rt["tel"]="N/A"
	
	pprint(rt)
	return rt
'''
while 1:
	data=read()
	if data==None or data["type"]!="location":
		continue
	get_search(data["lat"],data["long"],"restaurant")
	break
'''
