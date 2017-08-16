import telepot



bot=telepot.Bot('***REMOVED***')


def write(data,msg,keyboard=None):
	bot.sendMessage(data["chat_id"],msg)
	print("[\033[1;32msend\033[1;m]"+" Message sent to "+data["user"]+" \""+msg.replace("\n", "\\n")+"\"")

def answer_callback(data,msg=None):
	if msg==None:
		bot.answerCallbackQuery(data["update_id"])
		print("[\033[1;32msend\033[1;m]"+" Answered callback from "+data["user"])
	else:
		bot.answerCallbackQuery(data["update_id"],msg)
		print("[\033[1;32msend\033[1;m]"+" Answered callback from "+data["user"]+" with msg \""+msg.replace("\n", "\\n")+"\"")

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
				print("[\033[1;34mread\033[1;m]"+" Picture get from "+data["user"])
			elif "location" in raw["message"]:
				data["type"]="location"
				data["lat"]=raw["message"]["location"]["latitude"]
				data["long"]=raw["message"]["location"]["longitude"]
				print("[\033[1;34mread\033[1;m]"+" Location get from "+data["user"]+" with latitude "+str(data["lat"])+" and longtitude "+str(data["long"]))
			else:
				data["type"]="text"
				data["text"]=raw["message"]["text"]
				print("[\033[1;34mread\033[1;m]"+" Message get from "+data["user"]+" \""+data["text"].replace("\n", "\\n")+"\"")
		elif "callback_query" in raw:
			data["type"]="callback"
			data={"user_id":raw['callback_query']['from']['id'],"user":"","chat_id":raw['callback_query']['chat']["id"]}
			if "first_name" in raw['callback_query']['from']:
				data["user"]=data["user"]+raw['callback_query']['from']['first_name']
			if "last_name" in raw['callback_query']['from']:
				data["user"]=data["user"]+raw['callback_query']['from']['last_name']
			data["update_id"]=raw["update_id"]	
			data["data"]=raw["callback_query"]["data"]
			print("[\033[1;34mread\033[1;m]"+" Callback get from "+data["user"]+" \""+data["data"].replace("\n", "\\n")+"\"")
		else:
			return None


		return data
	else:
		return None
