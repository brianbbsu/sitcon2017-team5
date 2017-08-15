import re
import telepot
from pprint import pprint
from telepot.loop import MessageLoop


bot=telepot.Bot('425461487:AAE5JRdkXqrk9pRq54QDGd5-Xy2pU1tgCe4')

raw=bot.getUpdates()

if len(raw):
	bot.getUpdates(raw[-1]["update_id"]+1)

pprint(raw)
