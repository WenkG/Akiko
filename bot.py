import time
import telebot
import os

port = int(os.environ.get("PORT", 5000))
app.run(debug=True, host='0.0.0.0', port=port)
TOKEN = "1655376416:AAE5TZAtSNMnL_uwAofW7702yd4Fx_vuWgk"
bot = telebot.TeleBot(token=TOKEN)

def findat(msg):
    # from a list of texts, it finds the one with the '@' sign
    for i in msg:
        if '@' in i:
            return i

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Привет, я Акико!\n(⁄ ⁄>⁄ ▽ ⁄<⁄ ⁄)\nА как зовут тебя?~")


@bot.message_handler(func=lambda m: True) #????????
def acquaintance(message):
    name = message.text
    bot.send_message(message.chat.id, f"Очень приятно, {name}＼(≧▽≦)／")

@bot.message_handler(func=lambda msg: msg.text is not None and '@' in msg.text)
# lambda function finds messages with the '@' sign in them
# in case msg.text doesn't exist, the handler doesn't process it
def at_converter(message):
    texts = message.text.split()
    at_text = findat(texts)
    if at_text == '@': # in case it's just the '@', skip
        pass
    else:
        insta_link = "https://ancient-tor-24688.herokuapp.com/".format(at_text[1:])
        bot.reply_to(message, insta_link)

while True:
    try:
        bot.polling(none_stop=True)
        # ConnectionError and ReadTimeout because of possible timout of the requests library
        # maybe there are others, therefore Exception
    except Exception:
        time.sleep(15)