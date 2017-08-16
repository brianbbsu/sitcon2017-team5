import requests
import json
from pprint import pprint
import urllib
from bot import read

base="https://maps.googleapis.com/maps/api/place/nearbysearch/json?key=AIzaSyBeqKyY86QL_Ao23mEyDUGFuj7bjyag2Og&rankby=distance"

def get_search(lat,lng,tp):
	place="&location="+str(lat)+","+str(lng)+"&type="+tp
	raw=requests.get(base+place)
	js=json.loads(raw.text)
	pprint(js)

while 1:
	data=read()
	if data==None or data["type"]!="location":
		continue
	get_search(data["lat"],data["long"],"restaurant")
	break
