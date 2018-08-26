import json
from pprint import pprint
import requests

import datetime
from geopy.distance import vincenty
from tzwhere import tzwhere
import pytz

import conf

tz = tzwhere.tzwhere()

def get_location(s):
	
	complete_url = "https://maps.googleapis.com/maps/api/place/autocomplete/json"
	place_detail_url = "https://maps.googleapis.com/maps/api/place/details/json"

	raw = requests.get(complete_url, params={"key": conf.googlemap_apikey,"input": s})
	js=json.loads(raw.text)
	print(raw.url)

	if len(js["predictions"])==0:
		return None
	
	pid=js["predictions"][0]["place_id"]
	
	raw = requests.get(place_detail_url, params={"key": conf.googlemap_apikey,"placeid": pid})
	js=json.loads(raw.text)
	print(raw.url)
	
	rt={}
	
	rt["lat"]=js["result"]["geometry"]["location"]["lat"]
	rt["long"]=js["result"]["geometry"]["location"]["lng"]
	
	pprint(rt)
	return rt

def get_search(lat,lng,tp):
	nearby_search_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

	payload = {
		"key": conf.googlemap_apikey,
		"language": "zh-TW",
		"rankby": "distance",
		"location": "{},{}".format(lat,lng),
		"type": tp
	}

	raw=requests.get(nearby_search_url, params=payload)
	js=json.loads(raw.text)
	print(raw.url)
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

def get_detail(pid):
	global tz

	place_detail_url = "https://maps.googleapis.com/maps/api/place/details/json"

	payload = {
		"key": conf.googlemap_apikey,
		"language": "zh-TW",
		"placeid": pid
	}

	raw=requests.get(place_detail_url, params=payload)
	js=json.loads(raw.text)
	print(raw.url)
	
	rt={}

	rt["lat"]=js["result"]["geometry"]["location"]["lat"]
	rt["long"]=js["result"]["geometry"]["location"]["lng"]

	if "formatted_address" in js["result"]:
		rt["add"]=js["result"]["formatted_address"]
	else:
		rt["add"]="未知"

		
	if "formatted_phone_number" in js["result"]:
		rt["tel"]=str(js["result"]["formatted_phone_number"])
	else:
		rt["tel"]="未知"

	if "rating" in js["result"]:
		rt["rating"] = js["result"]["rating"]
		rt["rating_rounded"] = round(js["result"]["rating"])
		rt["rating_string"] = " " + ("%0.1f" % js["result"]["rating"]) + " / 5"
	else:
		rt["rating"] = 0
		rt["rating_rounded"] = 0
		rt["rating_string"] = "未知"
	
	if "permanently_closed" in js["result"]:
		rt["open"] = "永久停業"
	elif "opening_hours" in js["result"] and "open_now" in js["result"]["opening_hours"]:
		if  js["result"]["opening_hours"]["open_now"]:
			rt["open"] = "營業中"
		else:
			rt["open"] = "休息中"
		
		if "weekday_text" in js["result"]["opening_hours"]:
			txt = ["日","一","二","三","四","五","六"]
			tz_str = tz.tzNameAt(float(rt['lat']),float(rt['long']))
			weekday = int(datetime.datetime.now(pytz.timezone(tz_str)).strftime('%w'))
			for s in js["result"]["opening_hours"]["weekday_text"]:
				if s[2] == txt[weekday]:
					rt["open"] += " (" + s + ")"
	else:
		rt["open"] = "未知"
	
	pprint(rt)
	return rt