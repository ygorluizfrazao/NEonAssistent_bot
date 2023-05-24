import ast

import telebot
from telebot import types
from telebot.types import WebAppInfo

import BotImages
import Constants

TOKEN = Constants.API_KEY

bot = telebot.TeleBot(TOKEN, parse_mode=None)

MENU_PROGRAMACAO = "Programação             📅"
MENU_CONTEUDO = "Criação de conteúdo     📦"
MENU_INFORMACOES = "Informações do evento   ℹ️"
MENU_INGRESSOS = "Ingressos               🎫"
MENU_ENQUETES = "Enquetes                ☑️"

menu_command_dict = {
    MENU_PROGRAMACAO: "/programacao",
    MENU_CONTEUDO: "/conteudo",
    MENU_INFORMACOES: "/informacoes",
}

menu_apps_dict = {
    MENU_INGRESSOS: "https://t.me/NEonAssistent_bot/neon_ingressos",
    MENU_ENQUETES: "https://t.me/NEonAssistent_bot/enquetes"
}

user_menu_state = {}
waiting_photo_response = {}


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


def send_menu(chat_id):
    bot.send_message(chat_id=chat_id,
                     text="Veja o que podemos fazer por você:",
                     reply_markup=menu_markups())


@bot.message_handler(commands=['menu'])
def menu(message):
    send_menu(message.chat.id)


@bot.message_handler(commands=['start', 'iniciar', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id,
                     "Olá " + message.from_user.first_name + ", estou aqui para te ajudar com sua imersão no NEon "
                                                             "2023. Vamos lá?")
    send_menu(chat_id=message.chat.id)


@bot.message_handler(commands=['enquetes', 'ingressos'])
def open_app_by_command(message):
    print(message.text)
    if message.text == '/enquetes':
        user_menu_state[message.from_user.id] = MENU_ENQUETES
        bot.send_message(chat_id=message.chat.id,
                         text=menu_apps_dict[MENU_ENQUETES])
    if message.text == '/ingressos':
        user_menu_state[message.from_user.id] = MENU_INGRESSOS
        bot.send_message(chat_id=message.chat.id,
                         text=menu_apps_dict[MENU_INGRESSOS])


def print_hi(name):
    print(f'Hi, {name}')


def process_photo_message(message, file_path=None):
    # print('message.photo =', message.photo)
    # file_id = message.photo[-1].file_id
    # print('fileID =', file_id)
    if file_path is None:
        file_path = bot.get_file(message.photo[-1].file_id).file_path

    try:
        bot.reply_to(message, "Aguarde alguns segundos, estou fazendo algo incrível para você.")
        img_with_overlay = BotImages.img_overlay(
            'https://api.telegram.org/file/bot{0}/{1}'.format(TOKEN, file_path))
        bot.send_photo(chat_id=message.chat.id, reply_to_message_id=message, photo=img_with_overlay,
                       caption="Aqui está você no NordesteON!")
        bot.send_message(message.chat.id, "Compartilhe em suas redes sociais.")
    except BotImages.ImageUnreachable:
        bot.reply_to(message, "Desculpe, não consegui processar a imagem, tente novamente mais tarde.")
    finally:
        user_menu_state[message.from_user.id] = ""


@bot.message_handler(commands=['conteudo'])
def handle_conteudo_option(message):
    user_menu_state[message.from_user.id] = MENU_CONTEUDO
    bot.send_message(message.chat.id,
                     "Gostaria de uma foto personalizada com uma moldura exclusiva do NEon? Envie uma foto.")


@bot.message_handler(commands=['informacoes'])
def handle_informacoes(message):
    user_menu_state[message.from_user.id] = MENU_INFORMACOES
    bot.send_message(message.chat.id,
                     "Não perca o *NEon 2023* em *São Luís*!\n"
                     "Dias *01* e *02* de junho no Multicenter Sebrae.",
                     parse_mode="MARKDOWN")
    bot.send_message(chat_id=message.chat.id,
                     text="https://t.me/NEonAssistent_bot/info")
    bot.send_message(message.chat.id,
                     "Siga o *mapa*.",
                     parse_mode="MARKDOWN")
    bot.send_location(chat_id=message.chat.id, latitude=-2.5031943, longitude=-44.2675632)


@bot.message_handler(content_types=['photo'])
def photo(message):
    if message.from_user.id in user_menu_state and user_menu_state[message.from_user.id] == MENU_CONTEUDO:
        process_photo_message(message)
    else:
        waiting_photo_response[message.from_user.id] = message
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Sim", callback_data="['value', 'PS', 'PS']"))
        markup.add(types.InlineKeyboardButton("Não", callback_data="['value', 'PN', 'PN']"))
        bot.send_message(chat_id=message.chat.id,
                         text="Gostaria de uma foto personalizada com uma moldura exclusiva do NEon?",
                         reply_to_message_id=message,
                         reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    if call.data.startswith("['value'"):
        value_from_callback = ast.literal_eval(call.data)[1]
        key_from_callback = ast.literal_eval(call.data)[2]
        bot.answer_callback_query(callback_query_id=call.id)
        if key_from_callback == 'PS' and call.from_user.id in waiting_photo_response:
            user_menu_state[call.from_user.id] = MENU_CONTEUDO
            photo(waiting_photo_response[call.from_user.id])
            waiting_photo_response.pop(call.from_user.id)
            return
        if key_from_callback == 'PN':
            user_menu_state[call.from_user.id] = ""
            bot.send_message(call.message.chat.id, "Tudo bem, quando quiser utilizar este recurso, digite /conteudo.")
            if call.message.from_user.id in waiting_photo_response:
                waiting_photo_response.pop(call.from_user.id)

            return

        if key_from_callback in menu_apps_dict:
            user_menu_state[call.from_user.id] = key_from_callback
            bot.send_message(chat_id=call.message.chat.id,
                             text=menu_apps_dict[key_from_callback])
            return

        if key_from_callback in menu_command_dict:
            match menu_command_dict[key_from_callback]:
                case "/conteudo":
                    call.message.from_user.id = call.from_user.id
                    handle_conteudo_option(call.message)
                case "/informacoes":
                    call.message.from_user.id = call.from_user.id
                    handle_informacoes(call.message)


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    print(message)
    bot.reply_to(message, 'Desculpe, não entendi, essas são as opções que ofereço atualmente')
    user_menu_state[message.from_user.id] = ""
    send_menu(chat_id=message.chat.id)


if __name__ == '__main__':
    print_hi('PyCharm')

bot.infinity_polling()
