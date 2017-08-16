import re
from telepot.namedtuple import InlineKeyboardMarkup,InlineKeyboardButton
from bot import read,write,answer_callback

while True:


	data=read()

	if data==None:
		continue
	print(data)
	if data["type"]=="text":
		keyboard=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Ok",callback_data="btn_ok")]])
		write(data,"hi",keyboard)
	elif data["type"]=="location":
		write(data,"Thank you for your location")
	elif data["type"]=="callback":
		answer_callback(data)	
		write(data,"123")
	elif data["type"]=="pic":
		write(data,"this is a picture")
	else:
		write(data,"Unable to parse message.")

