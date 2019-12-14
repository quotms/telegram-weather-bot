import telebot
from datetime import date, timedelta

token = 'token here'

bot = telebot.TeleBot(token)
telebot.apihelper.proxy = {'https': 'socks5://proxy here'}
states = {}

MAIN_STATE = 'main'
WEATHER_DATE_STATE = 'weather_date_handler'

@bot.message_handler(func=lambda message: True)
def dispacther(message):
    print(states)
    user_id = message.from_user.id
    state = states.get(user_id, MAIN_STATE)
    print('current state', user_id, state)

    if state == MAIN_STATE:
        main_handler(message)
    elif state == WEATHER_DATE_STATE:
        weather_date(message)

def main_handler(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, 'Это бот-погода. Поможет узнать погоду в любом городе. Какой город интересует?')
        states[message.from_user.id] = WEATHER_DATE_STATE
    else:
        bot.reply_to(message, 'Я тебя не понял')

def weather_date(message):
    if 'москва' in message.text.lower():
        bot.send_message(message.from_user.id, 'Сейчас отличная погода!')
        states[message.from_user.id] = MAIN_STATE
    elif 'москва завтра' in message.text.lower():
        bot.send_message(message.from_user.id, 'Сейчас отличная погода!')
        states[message.from_user.id] = MAIN_STATE


bot.polling()
