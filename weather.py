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
    if weather_status.find('雲')!=-1:
        weather_text='天氣多變請攜帶雨具再出門'
    elif weather_status.find('晴')!=-1:
        weather_text='請注意防曬再出門，以免紫外線傷害皮膚'
    elif weather_status.find('雨')!=-1:
        weather_text='請攜帶雨具出門，注意淋濕感冒了'
    elif weather_status.find('雪')!=-1:
        weather_text='出門要注意保暖喔'

    writepic(data,"天氣:{}，氣溫:{}".format(weather_status,round(weather_temp) ),"http://openweathermap.org/img/w/{}.png".format(weather_icon))
    write(data,weather_text)
   # print(data,"天氣:{}，氣溫:{}，http://openweathermap.org/img/w/{}.png".format(weather_status,round(weather_temp),weather_icon ))
    #print(data,weather_text)
#data={'lat':'25.0214484','lon':'121.3178532'}
#weather(data)
