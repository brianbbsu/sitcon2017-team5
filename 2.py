import re

s=input()
s=s.strip()
print(s)

s=re.sub(r"\n",r" ",s)
s=re.sub(r' +',r' ',s)

s=s.split(" ")

try:
	if len(s)!=2:
		raise
	print(int(s[0])+int(s[1]))
except Exception:
	print("please input two valid number")

