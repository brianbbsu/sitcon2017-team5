import telepot
import conf
import time

bot=telepot.Bot(conf.telegrambot_token)


def write(data,msg,keyboard=None):
	print(time.ctime(),end=" ")
	if keyboard==None:
		bot.sendMessage(data["chat_id"],msg)
	else:
		bot.sendMessage(data["chat_id"],msg,reply_markup=keyboard)
	print("[\033[1;32msend\033[1;m]"+" Message sent to "+data["user"]+" \""+msg.replace("\n", "\\n")+"\"")

def writepic(data,msg,pic):
	print(time.ctime(),end=" ")
	bot.sendPhoto(data["chat_id"],pic,msg)
	print("[\033[1;32msend\033[1;m]"+" Pic sent to "+data["user"]+" \""+msg.replace("\n", "\\n")+"\"")

def answer_callback(data,msg=None):
	print(time.ctime(),end=" ")
	if msg==None:
		bot.answerCallbackQuery(data["callback_id"])
		print("[\033[1;32msend\033[1;m]"+" Answered callback from "+data["user"])
	else:
		bot.answerCallbackQuery(data["callback_id"],msg)
		print("[\033[1;32msend\033[1;m]"+" Answered callback from "+data["user"]+" with msg \""+msg.replace("\n", "\\n")+"\"")

def read():
	raw=bot.getUpdates()
	if len(raw):
		raw=raw[0]
		bot.getUpdates(raw["update_id"]+1)
		data={}
		if "message" in raw:
			print(time.ctime(),end=" ")
			data={"user_id":raw['message']['from']['id'],"user":"","chat_id":raw['message']['chat']["id"]}
			if "first_name" in raw['message']['from']:
				data["user"]=data["user"]+raw['message']['from']['first_name']
			if "last_name" in raw['message']['from']:
				data["user"]=data["user"]+raw['message']['from']['last_name']
			if "photo" in raw["message"] or "sticker" in raw["message"]:
				data["type"]="pic"
				print("[\033[1;34mread\033[1;m]"+" Picture get from "+data["user"])
			elif "location" in raw["message"]:
				data["type"]="location"
				data["lat"]=raw["message"]["location"]["latitude"]
				data["long"]=raw["message"]["location"]["longitude"]
				print("[\033[1;34mread\033[1;m]"+" Location get from "+data["user"]+" with latitude "+str(data["lat"])+" and longtitude "+str(data["long"]))
			elif "text" in raw["message"]:
				data["type"]="text"
				data["text"]=raw["message"]["text"]
				print("[\033[1;34mread\033[1;m]"+" Message get from "+data["user"]+" \""+data["text"].replace("\n", "\\n")+"\"")
			else:
				data["type"]="error"	
				print("[\033[1;34mread\033[1;m]"+" Bad request get from "+data["user"])
		elif "callback_query" in raw:
			print(time.ctime(),end=" ")
			data={"user_id":raw['callback_query']['from']['id'],"user":"","chat_id":raw['callback_query']["message"]["chat"]['id']}
			data["type"]="callback"
			if "first_name" in raw['callback_query']['from']:
				data["user"]=data["user"]+raw['callback_query']['from']['first_name']
			if "last_name" in raw['callback_query']['from']:
				data["user"]=data["user"]+raw['callback_query']['from']['last_name']
			data["callback_id"]=raw["callback_query"]["id"]	
			data["data"]=raw["callback_query"]["data"]
			print("[\033[1;34mread\033[1;m]"+" Callback get from "+data["user"]+" \""+data["data"].replace("\n", "\\n")+"\"")
		else:
			return None


		return data
	else:
		return None
