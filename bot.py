import telebot
import requests

bot = telebot.TeleBot("1693297545:AAERxCQfTasIwU2FwEOlV0PJ4bkVU8kjHow")

@bot.message_handler(commands=["start"])
def start (message):
	bot.send_message(message.chat.id,f"Hi I'm here @xxscary")
	
	
bot.polling()