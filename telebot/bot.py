import telepot



bot=telepot.Bot('425461487:AAE5JRdkXqrk9pRq54QDGd5-Xy2pU1tgCe4')


def write(data,msg):
	bot.sendMessage(data["chat_id"],msg)
	print("[\033[1;32msend\033[1;m]"+" Message sent to "+data["user"]+" \""+msg.replace("\n", "\\n")+"\"")

def read():
	raw=bot.getUpdates()
	if len(raw):
		raw=raw[0]
		bot.getUpdates(raw["update_id"]+1)
		data={"user_id":raw['message']['from']['id'],"user":"","chat_id":raw['message']['chat']["id"]}
		if "first_name" in raw['message']['from']:
			data["user"]=data["user"]+raw['message']['from']['first_name']
		if "last_name" in raw['message']['from']:
			data["user"]=data["user"]+raw['message']['from']['last_name']
		if "text" not in raw["message"]:
			data["type"]="pic"
			print("[\033[1;34mread\033[1;m]"+" Picture get from "+data["user"])
		else:
			data["type"]="text"
			data["text"]=raw["message"]["text"]
			print("[\033[1;34mread\033[1;m]"+" Message get from "+data["user"]+" \""+data["text"].replace("\n", "\\n")+"\"")
				


		return data
	else:
		return None
