import re
from bot import read,write,answer_callback

while True:


	data=read()

	if data==None:
		continue
	elif data["type"]=="text":
		write(data,"hi")
	elif data["type"]=="location":
		write(data,"Thank you for your location")
	elif data["type"]=="callback":
		answer_callback(data)	
		write(data,"123")
	elif data["type"]=="pic":
		write(data,"this is a picture")
	else:
		write(data,"Unable to parse message.")

