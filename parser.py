import re
from telepot.namedtuple import InlineKeyboardMarkup,InlineKeyboardButton
from bot import read,write,answer_callback,writepic
import gui
from search import get_search
from detail import get_detail


stat={}
loc = {}
tp={}
rt={}

while True:

	data=read()

	if data==None:
		continue
	print(data)
	uid=data["user_id"]
	if data["type"]=="text":
		if data["text"]=="/start":
			stat[uid]=0
			tp[uid]=""
			loc[uid] = {"lat":0,"long":0}
			gui.show_selection(data)
		elif uid not in stat or stat[uid]!=1:
			write(data,"請輸入/start來開始找食物")
		else:
			pass
	elif uid not in stat:
		write(data,"請輸入/start來開始找食物")
	elif data["type"]=="location":
		loc[uid]["lat"]=data["lat"]
		loc[uid]["long"]=data["long"]
		if tp[uid]!="":
			rt[uid]=get_search(loc[uid]["lat"],loc[uid]["long"],tp[uid])
			if rt[uid]==None:
				write(data,"Sorry, no enough information.")
			else: 
				gui.show_store(data,rt[uid])
		else:
			gui.show_selection(data)	
			
		#write(data,"Thank you for your location")
	elif data["type"]=="callback":
		answer_callback(data)	
		if data["data"][0:2]=="tp":
			tp[uid]=["bakery","cafe","restaurant","bar"][int(data["data"][2])]
			if loc[uid]["lat"]!=0 or loc[uid]["long"]!=0:
				rt[uid]=get_search(loc[uid]["lat"],loc[uid]["long"],tp[uid])
				if rt[uid]==None:
					write(data,"Sorry, no enough information.")
				else: 
					gui.show_store(data,rt[uid])
			else:
				write(data,"請傳送您的位置")
		elif data["data"]=="return1":
			gui.show_selection(data)	
		elif data["data"]=="return2":
			gui.show_store(data,rt[uid])
		elif data["data"]=="ok":
			pass
		else:
			t=int(data["data"][5])
			tmprt=get_detail(rt[uid][t]["id"])
			rt[uid][t]["add"]=tmprt["add"]
			rt[uid][t]["tel"]=tmprt["tel"]
			gui.show_information(data,rt[uid],t)

	elif data["type"]=="pic":
		write(data,"this is a picture")
		writepic(data,"This is also a picture","https://i.imgur.com/s5geZynl.jpg")
	else:
		write(data,"Unable to parse message.")

