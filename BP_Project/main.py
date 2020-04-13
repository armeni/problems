import config
import telebot
import json
from telebot import types
from core import coordinates, weather, information
from core.emoji import *

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    markup.row('Weather' + sun)
    markup.row('Time' + watch)
    markup.row('Coordinates' + coord)
    markup.row('Information about country' + info)
    bot.send_message(message.chat.id, "Hello, " + message.from_user.first_name + "! I'm bot-geographer!\n What do you want to know?", reply_markup=markup)

@bot.message_handler(commands=['help'])
def help(message):
    markup = types.ReplyKeyboardMarkup()
    markup.row('Weather' + sun)
    markup.row('Time' + watch)
    markup.row('Coordinates' + coord)
    markup.row('Information about country' + info)
    bot.send_message(message.chat.id, "Choose one of the following items!", reply_markup=markup)

w = 0

@bot.message_handler(regexp="Weather")
def menu1(message):
    global w
    bot.send_message(message.chat.id, "Enter the name of the city\nexample: London, United Kingdom")
    w = 1

@bot.message_handler(func = lambda message: w == 1)
def weather_request(message):
    global w
    w = 0
    bot.send_message(message.chat.id, weather.output(message.text))

c = 0

@bot.message_handler(regexp="Coordinates")
def menu2(message):
    global c
    bot.send_message(message.chat.id, "Enter the name of the city\nexample: London, United Kingdom")
    c = 1

@bot.message_handler(func = lambda message: c == 1)
def coord_request(message):
    global c
    c = 0
    bot.send_message(message.chat.id, coordinates.output(message.text))

p = 0

@bot.message_handler(regexp="Information about country")
def menu3(message):
    global p
    bot.send_message(message.chat.id, "Enter the name of the country")
    p = 1

@bot.message_handler(func = lambda message: p == 1)
def info_request(message):
    global p
    p = 0
    bot.send_message(message.chat.id, information.info(message.text))

if __name__ == '__main__':
    bot.polling(none_stop=True)