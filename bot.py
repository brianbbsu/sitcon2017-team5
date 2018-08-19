import telepot
import conf
import time
from logger import Logger

bot=telepot.Bot(conf.telegrambot_token)


def write(data,msg,keyboard=None):
	if keyboard==None:
		bot.sendMessage(data["chat_id"],msg)
	else:
		bot.sendMessage(data["chat_id"],msg,reply_markup=keyboard)
	Logger.log(Logger.SEND,"Message sent to %s \"%s\"",data['user'],msg.replace("\n", "\\n"))

def writepic(data,msg,pic):
	bot.sendPhoto(data["chat_id"],pic,msg)
	Logger.log(Logger.SEND,"Pic sent to %s \"%s\"",data['user'],msg.replace("\n", "\\n"))

def answer_callback(data,msg=None):
	if msg==None:
		bot.answerCallbackQuery(data["callback_id"])
		Logger.log(Logger.SEND,"Answered callback from %s",data["user"])
	else:
		bot.answerCallbackQuery(data["callback_id"],msg)
		Logger.log(Logger.SEND,"Answered callback from %s with msg \"%s\"",data["user"],msg.replace("\n", "\\n"))

def read():
	raw=bot.getUpdates()
	if len(raw):
		raw=raw[0]
		bot.getUpdates(raw["update_id"]+1)
		data={}
		if "message" in raw:
			data={"user_id":raw['message']['from']['id'],"user":"","chat_id":raw['message']['chat']["id"]}
			if "first_name" in raw['message']['from']:
				data["user"]=data["user"]+raw['message']['from']['first_name']
			if "last_name" in raw['message']['from']:
				data["user"]=data["user"]+raw['message']['from']['last_name']
			if "photo" in raw["message"] or "sticker" in raw["message"]:
				data["type"]="pic"
				Logger.log(Logger.READ,"Picture get from %s",data["user"])
			elif "location" in raw["message"]:
				data["type"]="location"
				data["lat"]=raw["message"]["location"]["latitude"]
				data["long"]=raw["message"]["location"]["longitude"]
				Logger.log(Logger.READ,"Location get from %s with latitude %s and longtitude %s",data["user"],str(data["lat"]),str(data["long"]))
			elif "text" in raw["message"]:
				data["type"]="text"
				data["text"]=raw["message"]["text"]
				Logger.log(Logger.READ,"Message get from %s \"%s\"",data["user"],data["text"].replace("\n", "\\n"))
			else:
				data["type"]="error"	
				Logger.log(Logger.READ,"Bad request get from %s",data["user"])
		elif "callback_query" in raw:
			data={"user_id":raw['callback_query']['from']['id'],"user":"","chat_id":raw['callback_query']["message"]["chat"]['id']}
			data["type"]="callback"
			if "first_name" in raw['callback_query']['from']:
				data["user"]=data["user"]+raw['callback_query']['from']['first_name']
			if "last_name" in raw['callback_query']['from']:
				data["user"]=data["user"]+raw['callback_query']['from']['last_name']
			data["callback_id"]=raw["callback_query"]["id"]	
			data["data"]=raw["callback_query"]["data"]
			Logger.log(Logger.READ,"Callback get from %s \"%s\"",data["user"],data["data"].replace("\n", "\\n"))
		else:
			return None


		return data
	else:
		return None
