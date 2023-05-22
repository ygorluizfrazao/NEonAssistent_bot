import ast

import telebot
from telebot import types
from telebot.types import WebAppInfo

import constants

TOKEN = constants.API_KEY

bot = telebot.TeleBot(TOKEN, parse_mode=None)

menu_command_dict = {
    "Programação": "/programacao",
    "Criação de conteúdo": "/conteudo",
    "Informações do evento": "/informacoes",
}

menu_apps_dict = {
    "Ingressos": "https://t.me/NEonAssistent_bot/neon_ingressos",
    "Enquetes": "https://t.me/NEonAssistent_bot/enquetes"
}


def menu_markups():
    markup = types.InlineKeyboardMarkup()

    for key, value in menu_command_dict.items():
        markup.add(types.InlineKeyboardButton(text=key,
                                              callback_data="['value', '" + value + "', '" + key + "']"))
    for key, value in menu_apps_dict.items():
        markup.add(types.InlineKeyboardButton(text=key,
                                              callback_data="['value', '" + key + "', '" + key + "']",
                                              url=value,
                                              web_app=WebAppInfo(url=value)))
    return markup


@bot.message_handler(commands=['menu'])
def send_menu(chat_id):
    bot.send_message(chat_id=chat_id,
                     text="Menu de opções",
                     reply_markup=menu_markups())


@bot.message_handler(commands=['start', 'iniciar', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Olá, sou o seu assistente do NordesteON, aqui estão as ações que posso executar:\n\n\n")
    send_menu(chat_id=message.chat.id)


@bot.message_handler(commands=['enquetes'])
def open_app_by_command(message):
    bot.send_message(chat_id=message.chat.id,
                     text=menu_apps_dict[message.text.replace('/', '').capitalize()])


def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    print_hi('PyCharm')


@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    if call.data.startswith("['value'"):
        # print(f"call: {call}")
        # print(f"call.data : {call.data} , type : {type(call.data)}")
        # print(
        #     f"ast.literal_eval(call.data) : {ast.literal_eval(call.data)} , type : {type(ast.literal_eval(call.data))}")

        value_from_callback = ast.literal_eval(call.data)[1]
        key_from_callback = ast.literal_eval(call.data)[2]
        # bot.answer_callback_query(callback_query_id=call.id,
        #                           text="You Clicked " + value_from_callback + " and key is " + key_from_callback)
        bot.answer_callback_query(callback_query_id=call.id)
        # bot.send_message(chat_id=call.message.chat.id,
        #                  text="You Clicked " + value_from_callback + " and key is " + key_from_callback)
        if key_from_callback in menu_apps_dict:
            bot.send_message(chat_id=call.message.chat.id,
                             text=menu_apps_dict[key_from_callback])


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    print(message)
    bot.reply_to(message, 'Desculpe, não entendi, essas são as opções que ofereço atualmente')
    send_menu(chat_id=message.chat.id)


bot.infinity_polling()
