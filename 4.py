import re
from bot import read,write

while True:


	data=read()

	if data==None:
		continue

	try:
		if data["type"]!="text":
			raise
		s=data["text"]
		if s[0]=='/':
			s=s[1: ].lower()
			if s == 'start':
				write(data,"Hello "+data["user"]+"\nThis is a bot made by briansu.\nPlease input two numbers\nand I'll add them up for you.")
			elif s=='help':
				write(data,"This is a bot made by briansu.\nPlease input two numbers\nand I'll add them up for you.")
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
				write(data,str(int(s[0])+int(s[1])))
			except Exception:
				write(data,"please input two valid number")
	except Exception:
		write(data,"Not a valid command")
