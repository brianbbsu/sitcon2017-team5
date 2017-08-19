import re
import telepot
from pprint import pprint


bot=telepot.Bot('342309989:AAFzdRL--BzhxFU3Wq_a6cLgJCul3KmjHfc')

raw=bot.getUpdates()

if len(raw):
	bot.getUpdates(raw[-1]["update_id"]+1)

pprint(raw)
