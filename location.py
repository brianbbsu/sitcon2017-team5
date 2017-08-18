import requests
import json
import urllib
from pprint import pprint
import conf

base="https://maps.googleapis.com/maps/api/place/autocomplete/json?key="+conf.googlemap_apikey+"&input="

base2="https://maps.googleapis.com/maps/api/place/details/json?key="+conf.googlemap_apikey+"&placeid="

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
