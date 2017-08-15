import re
import telepot
from pprint import pprint
from telepot.loop import MessageLoop


bot=telepot.Bot('425461487:AAE5JRdkXqrk9pRq54QDGd5-Xy2pU1tgCe4')


def write(user_id,msg):
	bot.sendMessage(user_id,msg)
	print(msg)


while True:

	raw=bot.getUpdates()

	if len(raw):
		bot.getUpdates(raw[-1]["update_id"]+1)

	for msg in raw:
		user_id=msg['message']['chat']['id']
		try:
			s=msg["message"]["text"]
			if s[0]=='/':
				s=s[1: ].lower()
				if s == 'start':
					write(user_id,"""\
Hello
123
""")
				elif s=='help':
					write(user_id,"hello123")
				else:
					raise
			else:
				s=s.strip()
				s=re.sub(r"\n",r" ",s)
				s=re.sub(r' +',r' ',s)

				s=s.split(" ")

				try:
					if len(s)!=2:
						raise
					write(user_id,str(int(s[0])+int(s[1])))
				except Exception:
					write(user_id,"please input two valid number")
		except Exception:
			write(user_id,"Not a valid command")
