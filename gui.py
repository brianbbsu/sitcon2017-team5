import telepot
import json
import time
from bot.py import write
from telepot.loop import MessageLoop
from telepot.namedtuple import (
    ReplyKeyboardMarkup, 
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

def show_selection(data, msg):
    header  = telepot.glance(msg, flavor="chat")
    if header[0] == "text":
        text = msg["text"]
        if text.startswith("/"):
            command = text.lstrip("/")
            if command == "hungry":
                text = "{}，讓我幫你找找食物！"
                bot.sendMessage(header[2], text.format(msg["from"]["last_name"]))

                replyKeyboard = InlineKeyboardMarkup(inline_keyboard=[
                    [InlineKeyboardButton(text="麵包店🍞",callback_data="bread")],
                    [InlineKeyboardButton(text="咖啡廳🍵",callback_data="coffee")],
                    [InlineKeyboardButton(text="餐廳🍛",callback_data="restaurant")],
                    [InlineKeyboardButton(text="酒吧🍺",callback_data="bar")],

                ])
                bot.sendMessage(header[2], text="要選擇什麼類型的食物呢？", reply_markup=replyKeyboard)


def show_store(data, msg, restaurant):
    header  = telepot.glance(msg, flavor="chat")
    
    if header[0] == "text":
        text = msg["text"]
        if text.startswith("/"):
            command = text.lstrip("/")
            if command == "hungry":
                replyKeyboard = InlineKeyboardMarkup(inline_keyboard=[
                    [InlineKeyboardButton(text="✔️" restaurant[0]['name'] "\n (距離：" restaurant[0]['dis'] "m)", callback_data="store0")],
                    [InlineKeyboardButton(text="✔️" restaurant[1]['name'] "\n (距離：" restaurant[1]['dis'] "m)", callback_data="store1")],
                    [InlineKeyboardButton(text="✔️" restaurant[2]['name'] "\n (距離：" restaurant[2]['dis'] "m)", callback_data="store2")],
                    [InlineKeyboardButton(text="✔️" restaurant[3]['name'] "\n (距離：" restaurant[3]['dis'] "m)", callback_data="store3")],
                    [InlineKeyboardButton(text="⤴️上一頁",callback_data="page")],
                ])
                bot.sendMessage(header[2], text="以下取距離最近的4家店家：", reply_markup=replyKeyboard)


def show_information(data, msg, restaurant, index):
    header  = telepot.glance(msg, flavor="chat")
    bot.sendMessage(header[2],  "以下為此店家的相關資訊：\n"
                                "🏠商家：" restaurant[]['name'] "\n"
                                "📞電話：" +" ---電話--- " + "\n"
                                "🚲距離：" restaurant[]['dis'] "\n"
                                "📝地址：" +" ---地址--- " + "\n")


TOKEN = '379698070:AAF6YVhUR24NtMhUZMTaf3y3RO406-coXPo'
bot = telepot.Bot(TOKEN)
MessageLoop(bot, {
    'chat':  show_selection}).run_as_thread()
print('Listening ...')

while 1:
    time.sleep(10)
