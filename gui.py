import json
import time
from bot import write,write_location
from telepot.namedtuple import (
    ReplyKeyboardMarkup, 
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

def show_selection(data):

    replyKeyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🍞 麵包店",callback_data="tp0")],
        [InlineKeyboardButton(text="☕️ 咖啡廳",callback_data="tp1")],
        [InlineKeyboardButton(text="🍛 餐廳",callback_data="tp2")],
        [InlineKeyboardButton(text="🍺 酒吧",callback_data="tp3")],
    ])
    write(data, "要選擇什麼類型的食物呢？",replyKeyboard)


def show_store(data, restaurant):
    
    replyKeyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="✔️" +  restaurant[0]['name'] +  "\n (" +  str(restaurant[0]['dis']) +  "m)", callback_data="store0")],
        [InlineKeyboardButton(text="✔️" +  restaurant[1]['name'] +  "\n (" +  str(restaurant[1]['dis']) +  "m)", callback_data="store1")],
        [InlineKeyboardButton(text="✔️" +  restaurant[2]['name'] +  "\n (" +  str(restaurant[2]['dis']) +  "m)", callback_data="store2")],
        [InlineKeyboardButton(text="✔️" +  restaurant[3]['name'] +  "\n (" +  str(restaurant[3]['dis']) +  "m)", callback_data="store3")],
        [InlineKeyboardButton(text="⤴️上一頁",callback_data="return1")],
    ])
    write(data, "以下為距離您最近的 4 家店家：", replyKeyboard)


def show_information(data, restaurant, index):
    replyKeyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⤴️上一頁",callback_data="return2")],
        [InlineKeyboardButton(text="👌OK",callback_data="OK")]
    ])
    write_location(data, restaurant[index]['name'],restaurant[index]['lat'], restaurant[index]['long'],restaurant[index]['add'])
    write(data, "以下為此店家的相關資訊：\n"
				"🏠 店名："+  restaurant[index]['name'] +  "\n"
				"📞 電話：" + restaurant[index]['tel'] + "\n"
                "🚲 距離："+  str(restaurant[index]['dis']) + "m\n"
                "📝 地址：" +restaurant[index]['add'] + "\n"
                         ,replyKeyboard)