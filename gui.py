import json
import time
from bot.py import write
from telepot.namedtuple import (
    ReplyKeyboardMarkup, 
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

def show_selection(data):

    text = "{}，讓我幫你找找食物！"
    write(data, text.format(data['user'])
    replyKeyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="麵包店🍞",callback_data="bread")],
        [InlineKeyboardButton(text="咖啡廳🍵",callback_data="coffee")],
        [InlineKeyboardButton(text="餐廳🍛",callback_data="restaurant")],
        [InlineKeyboardButton(text="酒吧🍺",callback_data="bar")],

    ])
    write(data, "要選擇什麼類型的食物呢？",replyKeyboard)


def show_store(data, restaurant):
    
    replyKeyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="✔️" restaurant[0]['name'] "\n (距離：" restaurant[0]['dis'] "m)", callback_data="store0")],
        [InlineKeyboardButton(text="✔️" restaurant[1]['name'] "\n (距離：" restaurant[1]['dis'] "m)", callback_data="store1")],
        [InlineKeyboardButton(text="✔️" restaurant[2]['name'] "\n (距離：" restaurant[2]['dis'] "m)", callback_data="store2")],
        [InlineKeyboardButton(text="✔️" restaurant[3]['name'] "\n (距離：" restaurant[3]['dis'] "m)", callback_data="store3")],
        [InlineKeyboardButton(text="⤴️上一頁",callback_data="return1")],
    ])
    write(data, "以下取距離最近的4家店家：", replyKeyboard)


def show_information(data, restaurant, index):
    replyKeyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⤴️上一頁",callback_data="return2")],
    ])
    write(data,  "以下為此店家的相關資訊：\n"
                                "🏠商家：" restaurant[index]['name'] "\n"
                                "📞電話：" +" ---電話--- " + "\n"
                                "🚲距離：" restaurant[index]['dis'] "\n"
                                "📝地址：" +" ---地址--- " + "\n"
                                ,replyKeyboard)

