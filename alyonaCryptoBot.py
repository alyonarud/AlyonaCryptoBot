import telebot
from extensions import APIException, Convertor_more
from config import TOKEN, keys, keys_more
import traceback

# alyonaCryptoBot



bot = telebot.TeleBot(TOKEN)


# Обрабатываются все сообщения, содержащие команды '/start' or '/help'.
@bot.message_handler(commands=['start', 'help'])
def start_help(message):
    text = "Для начала работы введите команду боту в следующем формате: \n " \
           "<имя или код валюты, цену которой хотите узнать>  <имя или код валюты, в которой надо узнать цену первой валюты> " \
           "<количество первой валюты>\n " \
           "Чтобы увидеть список доступных валют, введите команду /values  \n " \
           "Вводить названия валют можно как кодами, так и полными названиями, а можно и смешанные варианты"

    bot.reply_to(message, f"Приветствую, {message.chat.username} \n " + text)
#    pass

@bot.message_handler(commands=['values_old'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for i in keys.keys():
        text = '\n'.join((text, f"{i} - {keys[i]}"))
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for i in keys_more.keys():
        text = '\n'.join((text, f"{i} - {keys_more[i]}"))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def converter(message: telebot.types.Message):
    values = message.text.split(' ')
    try:
        if len(values) != 3:
            raise APIException('Неверное количество параметров!')

      #  answer = Convertor.get_price(*values)
        answer = Convertor_more.get_price(*values)
    except APIException as e:
        bot.reply_to(message, f"Ошибка в команде:\n{e}")
    except Exception as e:
        traceback.print_tb(e.__traceback__)
        bot.reply_to(message, f"Неизвестная ошибка:\n{e}")
    else:
        bot.reply_to(message, answer)

@bot.message_handler(content_types = ['voice',])
def repeat(message: telebot.types.Message):
    bot.reply_to(message, "мне нравится твой голос, только я ничего не понял!")

# Обрабатывается все документы и аудиозаписи
@bot.message_handler(content_types=['document', 'audio'])
def handle_docs_audio(message: telebot.types.Message):
    bot.send_message(message.chat.id, "что-то получил")

# Обрабатывается фото

@bot.message_handler(content_types=['photo', ])
def say_lmao(message: telebot.types.Message):
    bot.reply_to(message, 'фотка хорошая, но что мне с этим делать?')

bot.polling(none_stop=True)
