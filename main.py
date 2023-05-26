import ast
import datetime

import telebot
from telebot import types
from telebot.types import WebAppInfo
import Alarms

import BotImages
import Constants
import Palestras
import Utils
import pickle
import pprint

TOKEN = Constants.API_KEY

bot = telebot.TeleBot(TOKEN, parse_mode=None)

MENU_PALESTRAS = "Palestras                  📅"
MENU_CONTEUDO = "Criação de conteúdo        📦"
MENU_INFORMACOES = "Informações do evento      ℹ️"
MENU_INGRESSOS = "Ingressos                  🎫"
MENU_ENQUETES = "Enquetes                   ☑️"
MENU_SOBRE = "Sobre                      💻"

menu_command_dict = {
    MENU_PALESTRAS: "/palestras",
    MENU_CONTEUDO: "/conteudo",
    MENU_INFORMACOES: "/informacoes",
    MENU_SOBRE: "/sobre"
}

menu_apps_dict = {
    MENU_INGRESSOS: "https://t.me/NEonAssistent_bot/neon_ingressos",
    MENU_ENQUETES: "https://t.me/NEonAssistent_bot/enquetes"
}

user_menu_state = {}
waiting_photo_response = {}
alarms = {}


def load_alarms():
    try:
        with open(Constants.ALARMS_FILE, 'rb') as alarms_file:
            saved_alarms = pickle.load(alarms_file)
    except EOFError or FileNotFoundError:
        with open(Constants.ALARMS_FILE, 'wb') as alarms_file:
            saved_alarms = {}
            pickle.dump(alarms, alarms_file, protocol=pickle.HIGHEST_PROTOCOL)
    for user_id in saved_alarms:
        user_alarms = saved_alarms[user_id]
        for tpl in user_alarms:
            tag, alarmtime, palestra_tpl, chat_id = tpl

            def callback(_chat_id, palestra):
                time_in_minutes = Utils.dhms_to_minutes(
                    *Utils.convert_timedelta(
                        palestra.date_time - datetime.datetime.now())
                ).__str__()
                text = "Olá, a palestra *" + palestra.headline + "* começará em *" + time_in_minutes + " minutos*, no " \
                                                                                                       "auditório *" \
                       + palestra.local + "*."
                bot.send_message(chat_id=_chat_id, text=text, parse_mode="MARKDOWN")

            define_alarm(user_id, alarmtime, palestra_tpl, chat_id, save_to_file=False,
                         callback=callback)

    save_alarms_to_file()


def save_alarms_to_file():
    with open(Constants.ALARMS_FILE, 'wb') as outfile:
        pickle.dump(alarms, outfile, protocol=pickle.HIGHEST_PROTOCOL)


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
                     text="Veja o que posso fazer por você: ✔️",
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
    if message.text == '/enquetes':
        user_menu_state[message.from_user.id] = MENU_ENQUETES
        bot.send_message(chat_id=message.chat.id,
                         text=menu_apps_dict[MENU_ENQUETES])
    if message.text == '/ingressos':
        user_menu_state[message.from_user.id] = MENU_INGRESSOS
        bot.send_message(chat_id=message.chat.id,
                         text=menu_apps_dict[MENU_INGRESSOS])


def print_hi(name):
    print(f'Started from {name}')


def process_photo_message(message, file_path=None):
    if file_path is None:
        file_path = bot.get_file(message.photo[-1].file_id).file_path

    try:
        bot.reply_to(message, "Aguarde alguns segundos, estou fazendo algo incrível para você. 🕒🕒🕒")
        img_with_overlay = BotImages.img_overlay(
            'https://api.telegram.org/file/bot{0}/{1}'.format(TOKEN, file_path))
        bot.send_photo(chat_id=message.chat.id, reply_to_message_id=message, photo=img_with_overlay,
                       caption="Aqui está você no NordesteON!")
        bot.send_message(message.chat.id, "Compartilhe em suas redes sociais. 🤗🤗🤗")
    except BotImages.ImageUnreachable:
        bot.reply_to(message, "Desculpe, não consegui processar a imagem, tente novamente mais tarde.")
    finally:
        user_menu_state[message.from_user.id] = ""


@bot.message_handler(commands=['sobre'])
def handle_menu_sobre(message):
    bot.send_message(message.chat.id,
                     "Este bot foi desenvolvido por:\n\n"
                     "*Bruno Nunes Pinheiro*\n"
                     "Instagram: https://instagram.com/brunonunespinheiro\n"
                     "LinkedIn: https://www.linkedin.com/in/brunonunespinheiro/\n\n"
                     "*Ygor Luiz Frazão*\n"
                     "LinkedIn: https://www.linkedin.com/in/ygorluizfrazao/\n"
                     "Github: https://github.com/ygorluizfrazao\n"
                     "Portfólio: https://my-portfolio-livid-pi.vercel.app\n\n"
                     "Encomende o seu também!",
                     parse_mode="MARKDOWN")


@bot.message_handler(commands=['conteudo'])
def handle_conteudo_option(message):
    user_menu_state[message.from_user.id] = MENU_CONTEUDO
    bot.send_message(message.chat.id,
                     "Gostaria de uma foto personalizada com uma moldura exclusiva do NEon? Envie uma foto. 🤳")


@bot.message_handler(commands=['informacoes'])
def handle_informacoes(message):
    user_menu_state[message.from_user.id] = MENU_INFORMACOES
    bot.send_message(message.chat.id,
                     "Não perca o *NEon 2023* em *São Luís*!\n"
                     "Dias *01* e *02* de junho no Multicenter Sebrae. 📅",
                     parse_mode="MARKDOWN")
    bot.send_message(chat_id=message.chat.id,
                     text="https://t.me/NEonAssistent_bot/info")
    bot.send_message(message.chat.id,
                     "Siga o *mapa*. 🗺️",
                     parse_mode="MARKDOWN")
    bot.send_location(chat_id=message.chat.id, latitude=-2.5031943, longitude=-44.2675632)


def send_menu_palestras(message):
    markup = types.InlineKeyboardMarkup()

    for key in Palestras.palestras.keys():
        markup.add(types.InlineKeyboardButton(text=key,
                                              callback_data="['value', 'p', '" + key + "']"))
    bot.send_message(chat_id=message.chat.id,
                     text="Escolha um local para ver a programação",
                     reply_markup=markup,
                     parse_mode="MARKDOWN")


@bot.message_handler(commands=['palestras'])
def handle_palestras(message, detail_key=None):
    user_menu_state[message.from_user.id] = MENU_PALESTRAS
    if detail_key is not None:
        bot.send_message(chat_id=message.chat.id,
                         text="\n" + detail_key + "\n",
                         parse_mode="MARKDOWN")
        for idx, palestra in enumerate(Palestras.palestras[detail_key]):
            existing_alarm = return_first_tuple_if_alarm_exists(message.from_user.id, palestra)
            if existing_alarm is None:
                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton("Definir Lembrete ⏰",
                                                      callback_data="['value', '" + str(
                                                          idx) + "', '1" + detail_key + "']"))
                bot.send_message(chat_id=message.chat.id,
                                 text=palestra,
                                 reply_markup=markup,
                                 parse_mode="MARKDOWN")
            else:
                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton("Cancelar Lembrete 🔕",
                                                      callback_data="['value', '" + str(
                                                          idx) + "', '0" + detail_key + "']"))
                bot.send_message(chat_id=message.chat.id,
                                 text=palestra,
                                 reply_markup=markup,
                                 parse_mode="MARKDOWN")
    else:
        send_menu_palestras(message)


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
                         text="Gostaria de uma foto personalizada com uma moldura exclusiva do NEon? 🤳",
                         reply_to_message_id=message,
                         reply_markup=markup)


def define_alarm(user_id, alarmtime, palestra, chat_id, callback, save_to_file=True):
    def new_callback():
        callback(chat_id, palestra)
        remove_alarm(user_id, palestra, remover_from_scheduler=False)

    tag = Alarms.run_at(alarmtime, new_callback)
    if user_id in alarms:
        current_alarms = alarms[user_id]
        current_alarms.append((tag, alarmtime, palestra, chat_id))
        alarms[user_id] = current_alarms
    else:
        alarms[user_id] = [(tag, alarmtime, palestra, chat_id)]
    if save_to_file:
        save_alarms_to_file()


def return_first_tuple_if_alarm_exists(user_id, palestra):
    if user_id in alarms:
        current_alarms = alarms[user_id]
        for tpl in current_alarms:
            tag, alarmtime, palestra_tpl, chat_id = tpl
            if palestra.local == palestra_tpl.local and palestra_tpl.date_time_text == palestra.date_time_text:
                return tpl
    return None


def remove_alarm(user_id, palestra, remover_from_scheduler=True):
    while (to_remove := return_first_tuple_if_alarm_exists(user_id, palestra)) is not None:
        tag, alarmtime, palestra_tpl, chat_id = to_remove
        if remover_from_scheduler:
            Alarms.remove_schedule(tag)
        alarms[user_id].remove(to_remove)
        if not alarms[user_id]:
            alarms.pop(user_id)

    save_alarms_to_file()


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
            bot.send_message(call.message.chat.id, "Tudo bem, quando quiser utilizar este recurso, digite /conteudo. ✅")
            if call.message.from_user.id in waiting_photo_response:
                waiting_photo_response.pop(call.from_user.id)

            return

        if key_from_callback in Palestras.palestras:
            call.message.from_user.id = call.from_user.id
            handle_palestras(call.message, key_from_callback)

        if key_from_callback[1:] in Palestras.palestras:
            first_char = key_from_callback[0:1]
            palestra = Palestras.palestras[key_from_callback[1:]][int(value_from_callback)]
            existing_alarm = return_first_tuple_if_alarm_exists(call.from_user.id, palestra)
            if existing_alarm is None:
                if first_char == "1":

                    def callback(_chat_id, _palestra):
                        time_in_minutes = Utils.dhms_to_minutes(
                            *Utils.convert_timedelta(
                                _palestra.date_time - datetime.datetime.now())
                        ).__str__()
                        text = "Olá, a palestra *" + _palestra.headline + "* começará em *" + time_in_minutes + " minutos*, no " \
                                                                                                                "auditório *" \
                               + _palestra.local + "*."
                        bot.send_message(chat_id=_chat_id,
                                         text=text,
                                         parse_mode="MARKDOWN")

                    define_alarm(call.from_user.id,
                                 palestra.date_time - datetime.timedelta(minutes=15),
                                 palestra,
                                 chat_id=call.message.chat.id,
                                 callback=callback)
                    define_alarm(call.from_user.id,
                                 palestra.date_time - datetime.timedelta(minutes=2),
                                 palestra,
                                 chat_id=call.message.chat.id,
                                 callback=callback)
                    bot.reply_to(message=call.message,
                                 text="Lembrete definido para o evento.")
                elif first_char == "0":
                    bot.reply_to(message=call.message,
                                 text="Este lembrete já foi removido.")
            else:
                if first_char == "1":
                    markup = types.InlineKeyboardMarkup()
                    markup.add(types.InlineKeyboardButton("Cancelar Lembrete",
                                                          callback_data="['value', '" + value_from_callback + "', '0" + key_from_callback[
                                                                                                                        1:] + "']"))
                    bot.reply_to(message=call.message,
                                 text="Já existe lembrete definido para este evento, deseja cancelar?",
                                 reply_markup=markup,
                                 parse_mode="MARKDOWN")
                elif first_char == "0":
                    remove_alarm(call.from_user.id, palestra)
                    bot.reply_to(message=call.message,
                                 text="Lembrete removido para o evento.")

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
                case "/palestras":
                    call.message.from_user.id = call.from_user.id
                    handle_palestras(call.message)
                case "/sobre":
                    call.message.from_user.id = call.from_user.id
                    handle_menu_sobre(call.message)


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, 'Desculpe, não entendi, essas são as opções que ofereço atualmente')
    user_menu_state[message.from_user.id] = ""
    send_menu(chat_id=message.chat.id)


if __name__ == '__main__':
    print_hi('PyCharm')

load_alarms()
pprint.pprint(alarms)
Alarms.start()

bot.infinity_polling()
