import re
import telepot
from pprint import pprint


bot=telepot.Bot('***REMOVED***')

raw=bot.getUpdates()

if len(raw):
	bot.getUpdates(raw[-1]["update_id"]+1)

pprint(raw)
