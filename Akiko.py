import telebot;
bot = telebot.TeleBot('1655376416:AAE5TZAtSNMnL_uwAofW7702yd4Fx_vuWgk');


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Привет, я Акико!\n(⁄ ⁄>⁄ ▽ ⁄<⁄ ⁄)\nА как зовут тебя?~")


@bot.message_handler(func=lambda m: True) #????????
def acquaintance(message):
    name = message.text
    bot.send_message(message.chat.id, f"Очень приятно, {name}＼(≧▽≦)／\nАга, а на деле ты {message.from_user.first_name}, блять. Так всегда в интернете...")
    # bot.reply_to(message, message.text)

bot.polling()

# @bot.message_handler(content_types=['text'])
# def get_text_messages(message):
#     @bot.message_handler(content_types=['text', 'document', 'audio'])
#
# if message.text == "Привет":
#     bot.send_message(message.from_user.id, "Привет, я Акико. (⁄ ⁄>⁄ ▽ ⁄<⁄ ⁄) А как зовут тебя?~")
# elif message.text == "/help":
#     bot.send_message(message.from_user.id, "Напиши привет")
# else:
#     bot.send_message(message.from_user.id, "Извини, я тебя не понимаю... (╥﹏╥) Напиши /help.")
#
# bot.polling(none_stop=True, interval=0)