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
from logger import Logger

class Parser:
    def __init__(self):
        self.stat={}
        self.loc = {}
        self.tp={}
        self.rt={}
        self.running = True
        

    def reset(self,uid):
        self.stat.pop(uid,None)
        self.loc.pop(uid,None)
        self.tp.pop(uid,None)
        self.rt.pop(uid,None)


    def run(self):
        while True:
            try:
            
                data=read()

                if not self.running:
                    return

                if data==None:
                    continue
                print(data)
                uid=data["user_id"]
                if data["type"]=="text":
                    if data["text"]=="/start":
                        self.stat[uid]=0
                        self.tp[uid]=""
                        self.loc[uid] = {"lat":0,"long":0}
                        self.rt[uid]=[]
                        text = "{}，讓我幫你找找食物！\n""請輸入您所在的位置或是傳送手機的定位資訊："
                        write(data, text.format(data['user']))
                        #gui.show_selection(data)
                    elif uid not in self.stat or self.stat[uid]!=0:
                        if data["text"].find("安安")!=-1:
                            write(data,"安安你好，想吃些什麼呢?")
                        if data["text"].find("互相傷害")!=-1:
                            write(data,"好阿來互相傷害阿")
                        write(data,"請輸入 /start 來開始找食物")
                    else:
                        tmp=get_location(data["text"])
                        if tmp==None:
                            write(data,"Sorry, no enough information.")
                            self.reset(uid)	
                        else:
                            self.loc[uid]=tmp
                            self.stat[uid]=1
                            gui.show_selection(data)
                elif uid not in self.stat:
                    write(data,"請輸入 /start 來開始找食物")
                elif data["type"]=="location":
                    self.loc[uid]["lat"]=data["lat"]
                    self.loc[uid]["long"]=data["long"]
                    self.stat[uid]=1
                    if self.tp[uid]!="":
                        self.rt[uid]=get_search(self.loc[uid]["lat"],self.loc[uid]["long"],self.tp[uid])
                        if self.rt[uid]==None:
                            write(data,"Sorry, no enough information.")
                        else: 
                            gui.show_store(data,self.rt[uid])
                    else:
                        gui.show_selection(data)	
                        
                    #write(data,"Thank you for your location")
                elif data["type"]=="callback":
                    answer_callback(data)	
                    if data["data"][0:2]=="tp":
                        self.tp[uid]=["bakery","cafe","restaurant","bar"][int(data["data"][2])]
                        if self.stat[uid]!=0:
                            self.rt[uid]=get_search(self.loc[uid]["lat"],self.loc[uid]["long"],self.tp[uid])
                            if self.rt[uid]==None:
                                write(data,"Sorry, no enough information.")
                            else: 
                                gui.show_store(data,self.rt[uid])
                        else:
                            write(data,"請傳送您的位置")
                    elif data["data"]=="return1":
                        gui.show_selection(data)	
                    elif data["data"]=="return2":
                        gui.show_store(data,self.rt[uid])
                    elif data["data"]=="OK":
                        write(data,"以下是現在的天氣狀況：")
                        data["lat"]=self.loc[uid]["lat"]
                        data["long"]=self.loc[uid]["long"]
                        weather(data)
                        write(data,"祝你有個美好的用餐時光~")
                        self.reset(uid)
                    else:
                        t=int(data["data"][5])
                        tmprt=get_detail(self.rt[uid][t]["id"])
                        self.rt[uid][t]["add"]=tmprt["add"]
                        self.rt[uid][t]["tel"]=tmprt["tel"]
                        gui.show_information(data,self.rt[uid],t)

                elif data["type"]=="pic":
                    write(data,"this is a picture")
                    writepic(data,"This is also a picture","https://i.imgur.com/s5geZynl.jpg")
                else:
                    write(data,"Unable to parse message.")
            except KeyboardInterrupt:
                raise
            except:
                Logger.log(Logger.ERROR,"%s",str(sys.exc_info()))
        
    def stop(self):
        print("Stopping")
        self.running = False
