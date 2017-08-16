import re
from telepot.namedtuple import InlineKeyboardMarkup,InlineKeyboardButton
from bot import read,write,answer_callback,writepic
import gui
from search import get_search

while True:


	data=read()

	if data==None:
		continue
	print(data)
	if data["type"]=="text":
		keyboard=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Ok",callback_data="btn_ok")]])
		write(data,"hi",keyboard)
	elif data["type"]=="location":
		rt=get_search(data["lat"],data["long"],"restaurant")
		gui.show_store(data,rt)
		#write(data,"Thank you for your location")
	elif data["type"]=="callback":
		answer_callback(data)	
		write(data,"123")
	elif data["type"]=="pic":
		write(data,"this is a picture")
		writepic(data,"This is also a picture","https://i.imgur.com/s5geZynl.jpg")
	else:
		write(data,"Unable to parse message.")

