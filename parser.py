import re
from telepot.namedtuple import InlineKeyboardMarkup,InlineKeyboardButton
from bot import read,write,answer_callback,writepic
import gui
from search import get_search
from detail import get_detail
from location import get_location
from weather import weather
import sys
import time

stat={}
loc = {}
tp={}
rt={}

def reset(uid):
	stat.pop(uid,None)
	loc.pop(uid,None)
	tp.pop(uid,None)
	rt.pop(uid,None)


while True:

	try:
	
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
				rt[uid]=[]
				text = "{}，讓我幫你找找食物！\n""請輸入您所在的位置或是傳送手機的定位資訊："
				write(data, text.format(data['user']))
				#gui.show_selection(data)
			elif uid not in stat or stat[uid]!=0:
				if data["text"].find("安安")!=-1:
					write(data,"安安你好，想吃些什麼呢?")
				if data["text"].find("互相傷害")!=-1:
					write(data,"好阿來互相傷害阿")
				write(data,"請輸入/start來開始找食物")
			else:
				tmp=get_location(data["text"])
				if tmp==None:
					write(data,"Sorry, no enough information.")
					reset(uid)	
				else:
					loc[uid]=tmp
					stat[uid]=1
					gui.show_selection(data)
		elif uid not in stat:
			write(data,"請輸入/start來開始找食物")
		elif data["type"]=="location":
			loc[uid]["lat"]=data["lat"]
			loc[uid]["long"]=data["long"]
			stat[uid]=1
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
				if stat[uid]!=0:
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
			elif data["data"]=="OK":
				write(data,"以下是現在的天氣狀況：")
				data["lat"]=loc[uid]["lat"]
				data["long"]=loc[uid]["long"]
				weather(data)
				write(data,"祝你有個美好的用餐時光~")
				reset(uid)
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
	except KeyboardInterrupt:
		raise;
	except:
		print(time.ctime()+" \033[1;31mUnexpected error: "+str(sys.exc_info())+"\033[1;m")
