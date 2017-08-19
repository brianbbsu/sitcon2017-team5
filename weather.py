import requests
import json
from bot import write,writepic
def weather(data):
    lat=data["lat"]
    lon=data["lon"]
    weather_a=requests.get("http://api.openweathermap.org/data/2.5/weather?lang=zh_tw&units=metric&lat={}&lon={}&appid=9ec4e2aec0d50139161b0722fc392f15".format(lat,lon))
    weather_bot=json.loads(weather_a.text)
    for weather_bot2 in weather_bot["weather"]:
        weather_status=weather_bot2["description"]
        weather_icon=weather_bot2['icon']
    weather_temp=weather_bot["main"]["temp"]
    writepic(data,"天氣:{}，氣溫:{}".format(weather_status,round(weather_temp) ),"http://openweathermap.org/img/w/{}.png".format(weather_icon))
    #print(data,"天氣:{}，氣溫:{}，http://openweathermap.org/img/w/{}.png".format(weather_status,round(weather_temp),weather_icon ))
#data={'lat':'25.0214484','lon':'121.3178532'}
#weather(data)