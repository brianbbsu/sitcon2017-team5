import re
from telepot.namedtuple import InlineKeyboardMarkup,InlineKeyboardButton
from bot import read,write,answer_callback,writepic
import gui
from search import get_search
from detail import get_detail


stat=0
loc = {"lat":0,"long":0}
tp=""
rt=[]

while True:

	data=read()

	if data==None:
		continue
	print(data)
	if data["type"]=="text":
		if data["text"]=="/start":
			stat=0
			tp=""
			loc = {"lat":0,"long":0}
			gui.show_selection(data)
		else:
			write(data,"請輸入/start來開始找食物")
	elif data["type"]=="location":
		loc["lat"]=data["lat"]
		loc["long"]=data["long"]
		if tp!="":
			rt=get_search(loc["lat"],loc["long"],tp)
			if rt==None:
				write(data,"Sorry, no enough information.")
			else: 
				gui.show_store(data,rt)
		else:
			gui.show_selection(data)	
			
		#write(data,"Thank you for your location")
	elif data["type"]=="callback":
		answer_callback(data)	
		if data["data"][0:2]=="tp":
			tp=["bakery","cafe","restaurant","bar"][int(data["data"][2])]
			if loc["lat"]!=0 or loc["long"]!=0:
				rt=get_search(loc["lat"],loc["long"],tp)
				if rt==None:
					write(data,"Sorry, no enough information.")
				else: 
					gui.show_store(data,rt)
			else:
				write(data,"請傳送您的位置")
		elif data["data"]=="return1":
			gui.show_selection(data)	
		elif data["data"]=="return2":
			gui.show_store(data,rt)
		elif data["data"]=="ok":
			pass
		else:
			t=int(data["data"][5])
			tmprt=get_detail(rt[t]["id"])
			rt[t]["add"]=tmprt["add"]
			rt[t]["tel"]=tmprt["tel"]
			gui.show_information(data,rt,t)

	elif data["type"]=="pic":
		write(data,"this is a picture")
		writepic(data,"This is also a picture","https://i.imgur.com/s5geZynl.jpg")
	else:
		write(data,"Unable to parse message.")

