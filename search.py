import requests
import json
import urllib
from bot import read
from geopy.distance import vincenty
from pprint import pprint
import conf

base="https://maps.googleapis.com/maps/api/place/nearbysearch/json?key="+conf.googlemap_apikey2+"&rankby=distance"#&opennow=1"

def get_search(lat,lng,tp):
	place="&location="+str(lat)+","+str(lng)+"&type="+tp
	raw=requests.get(base+place)
	js=json.loads(raw.text)
	#pprint(js)
	print(base+place)
	if len(js["results"]) < 4:
		return None
	else:
		rt=[]
		for i in range(0,4):
			dt=js["results"][i]
			tmp={}
			tmp["lat"]=dt["geometry"]["location"]["lat"]
			tmp["long"]=dt["geometry"]["location"]["lng"]
			tmp["name"]=dt["name"]
			tmp["id"]=dt["place_id"]
			tmp["dis"]=int(vincenty((lat,lng),(tmp["lat"],tmp["long"])).meters)
			rt.append(tmp)
		pprint(rt)
	return rt
