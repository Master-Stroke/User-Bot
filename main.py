from pyrogram import Client, filters
from pyrogram.errors import FloodWait
 
from pyrogram.types import ChatPermissions
from pyrogram import Client
import time
from time import sleep
import random
import pyautogui
from random import shuffle
import os
from datetime import datetime

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.raw import functions

api_id = Your api_id
api_hash = "Your api_hash"

app = Client("my_account", api_id=api_id, api_hash=api_hash)

REPLACEMENT_MAP = {
    'А':'ɐ',
    'Б':'ƍ',
    'В':'ʚ',
    'Г':'ɹ',
    'Д':'ɓ',
    'Е':'ǝ',
    'Ё':'ǝ',
    'Ж':'ж',
    'З':'ε',
    'И':'и',
    'Й':'ņ',
    'К':'ʞ',
    'Л':'v',
    'М':'w',
    'Н':'н',
    'О':'о',
    'П':'u',
    'Р':'d',
    'С':'ɔ',
    'Т':'ɯ',
    'У':'ʎ',
    'Ф':'ф',
    'Х':'х',
    'Ц':'ǹ',
    'Ч':'Һ',
    'Ш':'m',
    'Щ':'m',
    'Ъ':'q',
    'Ь':'q',
    'Э':'є',
    'Я':'ʁ',
    'а':'ɐ',
    'б':'ƍ',
    'в':'ʚ',
    'г':'ɹ',
    'д':'ɓ',
    'е':'ǝ',
    'ё':'ǝ',
    'ж':'ж',
    'з':'ε',
    'и':'и',
    'й':'ņ',
    'к':'ʞ',
    'л':'v',
    'м':'w',
    'н':'н',
    'о':'о',
    'п':'u',
    'р':'d',
    'с':'ɔ',
    'т':'ɯ',
    'у':'ʎ',
    'ф':'ф',
    'х':'х',
    'ц':'ǹ',
    'ч':'Һ',
    'ш':'m',
    'щ':'m',
    'ъ':'q',
    'ь':'q',
    'э':'є',
    'я':'ʁ',
    "a": "ɐ",
    "b": "q",
    "c": "ɔ",
    "d": "p",
    "e": "ǝ",
    "f": "ɟ",
    "g": "ƃ",
    "h": "ɥ",
    "i": "ᴉ",
    "j": "ɾ",
    "k": "ʞ",
    "l": "l",
    "m": "ɯ",
    "n": "u",
    "o": "o",
    "p": "d",
    "q": "b",
    "r": "ɹ",
    "s": "s",
    "t": "ʇ",
    "u": "n",
    "v": "ʌ",
    "w": "ʍ",
    "x": "x",
    "y": "ʎ",
    "z": "z",
    "A": "∀",
    "B": "B",
    "C": "Ɔ",
    "D": "D",
    "E": "Ǝ",
    "F": "Ⅎ",
    "G": "פ",
    "H": "H",
    "I": "I",
    "J": "ſ",
    "K": "K",
    "L": "˥",
    "M": "W",
    "N": "N",
    "O": "O",
    "P": "Ԁ",
    "Q": "Q",
    "R": "R",
    "S": "S",
    "T": "┴",
    "U": "∩",
    "V": "Λ",
    "W": "M",
    "X": "X",
    "Y": "⅄",
    "Z": "Z",
    "0": "0",
    "1": "Ɩ",
    "2": "ᄅ",
    "3": "Ɛ",
    "4": "ㄣ",
    "5": "ϛ",
    "6": "9",
    "7": "ㄥ",
    "8": "8",
    "9": "6",
    ",": "'",
    ".": "˙",
    "?": "¿",
    "!": "¡",
    '"': ",,",
    "'": ",",
    "(": ")",
    ")": "(",
    "[": "]",
    "]": "[",
    "{": "}",
    "}": "{",
    "<": ">",
    ">": "<",
    "&": "⅋",
    "_": "‾",
}

# Command type
@app.on_message(filters.command("type", prefixes="."))
def type(_, msg):
    orig_text = msg.text.split(".type ", maxsplit=1)[1]
    text = orig_text
    tbp = "" # to be printed
    typing_symbol = "▒"
 
    while(tbp != orig_text):
        try:
            msg.edit(tbp + typing_symbol)
            sleep(0.05) # 50 ms
 
            tbp = tbp + text[0]
            text = text[1:]
 
            msg.edit(tbp)
            sleep(0.05)
 
        except FloodWait as e:
            sleep(e.x)
 
# Command vzlom pentagon
@app.on_message(filters.command("hack", prefixes="."))
def hack(_, msg):
    perc = 0
 
    while(perc < 100):
        try:
            text = "👮‍ Взлом пентагона в процессе ..." + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(1, 3)
            sleep(0.1)
 
        except FloodWait as e:
            sleep(e.x)
 
    msg.edit("🟢 Пентагон успешно взломан!")
    sleep(3)
 
    msg.edit("👽 Поиск секретных данных об НЛО ...")
    perc = 0
 
    while(perc < 100):
        try:
            text = "👽 Поиск секретных данных об НЛО ..." + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(1, 5)
            sleep(0.15)
 
        except FloodWait as e:
            sleep(e.x)
 
    msg.edit("🦖 Найдены данные о существовании динозавров на земле!")

@app.on_message(filters.command("flip", prefixes="."))
def flip(_, msg):
    text = msg.text.split(".flip", maxsplit=1)[1]
    final_str = ""
    for char in text:
        if char in REPLACEMENT_MAP.keys():
            new_char = REPLACEMENT_MAP[char]
        else:
            new_char = char
        final_str += new_char
    if text != final_str:
        msg.edit(final_str)
    else:
        msg.edit(text)

@app.on_message(filters.command("thanos", prefixes="."))
def thanos(_, msg):
    chat = msg.text.split(".thanos ", maxsplit=1)[1]
 
    members = [
        x
        for x in app.iter_chat_members(chat)
        if x.status not in ("administrator", "creator")
    ]
 
    random.shuffle(members)
 
    app.send_message(chat, "Щелчок Таноса ... *щёлк*")
 
    for i in range(len(members) // 2):
        try:
            app.restrict_chat_member(
                chat_id=chat,
                user_id=members[i].user.id,
                permissions=ChatPermissions(),
                until_date=int(time.time() + 86400),
            )
            app.send_message(chat, "Исчез " + members[i].user.first_name)
        except FloodWait as e:
            print("> waiting", e.x, "seconds.")
            time.sleep(e.x)
 
    app.send_message(chat, "Но какой ценой?")
 
app.run()
