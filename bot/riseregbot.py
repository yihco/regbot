# -*- coding: utf-8 -*-

# Telegram API
import telebot.async_telebot as atelebot
from telebot import types
# Configuration files
import config as cnf
from assets import phrases
# Tools
import asyncio

bot = atelebot.AsyncTeleBot(cnf.token, parse_mode='html')

@bot.message_handler(commands=['start'])
async def start(msg: types.Message):
    if not msg.from_user.is_bot and msg.from_user.id > 0:
        await bot.send_message(msg.chat.id, phrases.welcome['ru'])

asyncio.run(bot.polling(non_stop=False))