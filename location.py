import requests
import json
import urllib
from pprint import pprint

base="https://maps.googleapis.com/maps/api/place/autocomplete/json?key=AIzaSyBeqKyY86QL_Ao23mEyDUGFuj7bjyag2Og&input="

base2="https://maps.googleapis.com/maps/api/place/details/json?key=AIzaSyBeqKyY86QL_Ao23mEyDUGFuj7bjyag2Og&placeid="

def get_location(s):
	
	raw=requests.get(base+urllib.parse.quote(s))
	js=json.loads(raw.text)
	#pprint(js)
	print(base+s)

	if len(js["predictions"])==0:
		return None
	
	pid=js["predictions"][0]["place_id"]

	
	raw=requests.get(base2+str(pid))
	js=json.loads(raw.text)
	#pprint(js)
	print(base2+str(pid))
	
	rt={}
	
	rt["lat"]=js["result"]["geometry"]["location"]["lat"]
	rt["long"]=js["result"]["geometry"]["location"]["lng"]

	
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
