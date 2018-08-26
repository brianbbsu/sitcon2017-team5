import requests
import json
import urllib
import datetime
from tzwhere import tzwhere
import pytz
from bot import read
from pprint import pprint
import conf

base="https://maps.googleapis.com/maps/api/place/details/json?language=zh-TW&key="+conf.googlemap_apikey+"&placeid="

tz = tzwhere.tzwhere()

def get_detail(pid):
	raw=requests.get(base+str(pid))
	js=json.loads(raw.text)
	#pprint(js)
	print(base+str(pid))
	
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
