import sys
import time

from bot import read, write, answer_callback, writepic
import gui
from logger import Logger
from map_utils import get_location, get_search, get_detail
from weather import weather

class Parser:
    def __init__(self):
        self.location = {}
        self.place_type = {}
        self.result_list={}
        self.running = True
        
    def reset(self,uid):
        self.location.pop(uid,None)
        self.place_type.pop(uid,None)
        self.result_list.pop(uid,None)


    def run(self):
        while True:
            try:
                data=read()

                if not self.running:
                    return

                if data == None or data["type"] == "error":
                    continue

                print(data)

                uid = data["user_id"]
                if data["type"] == "text":
                    if data["text"].startswith("/"):
                        write(data,"請直接輸入您所在的位置或是傳送手機的定位資訊\n我將會幫你搜尋附近的食物：")
                    else:
                        tmp=get_location(data["text"])
                        if tmp==None:
                            write(data,"抱歉，您所提供的地點資料不足")
                        else:
                            self.location[uid]=tmp
                            gui.show_selection(data)

                elif data["type"] == "location":
                    self.location[uid] = {}
                    self.location[uid]["lat"]=data["lat"]
                    self.location[uid]["long"]=data["long"]
                    gui.show_selection(data)
                        
                elif data["type"] == "callback":
                    answer_callback(data)	
                    if uid not in self.location or self.location[uid] is None:
                        write(data,"請直接輸入您所在的位置或是傳送手機的定位資訊\n我將會幫你搜尋附近的食物：")
                    elif data["data"][0:2] == "tp":
                        self.place_type[uid] = ["bakery","cafe","restaurant","bar"][int(data["data"][2])]
                        self.result_list[uid]=get_search(self.location[uid]["lat"],self.location[uid]["long"],self.place_type[uid])
                        if self.result_list[uid]==None:
                            write(data,"抱歉，無法找到符合條件的搜尋結果")
                        else: 
                            gui.show_stores(data,self.result_list[uid])
                    elif data["data"]=="return1":
                        gui.show_selection(data)
                    elif uid not in self.result_list or self.result_list[uid] is None:
                        write(data,"請直接輸入您所在的位置或是傳送手機的定位資訊\n我將會幫你搜尋附近的食物：")
                    elif data["data"]=="return2":
                        gui.show_stores(data,self.result_list[uid])
                    elif data["data"]=="OK":
                        write(data,"以下是現在的天氣狀況：")
                        data["lat"]=self.location[uid]["lat"]
                        data["long"]=self.location[uid]["long"]
                        weather(data)
                        write(data,"祝你有個美好的用餐時光~")
                        self.reset(uid)
                    else:
                        t=int(data["data"][5])
                        if t >= len(self.result_list[uid]):
                            write(data,"請直接輸入您所在的位置或是傳送手機的定位資訊\n我將會幫你搜尋附近的食物：")
                        else:
                            tmprt=get_detail(self.result_list[uid][t]["id"])
                            self.result_list[uid][t].update(tmprt)
                            gui.show_information(data,self.result_list[uid],t)
                else:
                    write(data,"請直接輸入您所在的位置或是傳送手機的定位資訊\n我將會幫你搜尋附近的食物：")
            except:
                Logger.log(Logger.ERROR,"%s",str(sys.exc_info()))
        
    def stop(self):
        print("Stopping")
        self.running = False
