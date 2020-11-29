import time
import wikipedia
from telebot import TeleBot, types

bot_token = ''  # Paste your token API
bot = TeleBot(token=bot_token)
error = 'Wrong word, use /suggest'
word = " for the word..."


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(chat_id=message.chat.id, text='Greetings! Welcome, I am WikiBot.', reply_markup=main_keyboard())


@bot.message_handler(commands=['extra'])
def send_welcome(message):
    text = '<b>Extra Commands</b> \n' \
           '/purpose - shows the purpose why I was made\n' \
           '/dev - provides information about my creator\n' \
           '/source - my source code'
    bot.send_message(chat_id=message.chat.id, text=text, parse_mode='html', reply_markup=main_extra())


@bot.message_handler(commands=['big'])
def send_welcome(message):
    text = '/definitions - Complete wiki page of the word\n' \
           '/titles - All related & suggested titles'
    bot.send_message(chat_id=message.chat.id, text=text, parse_mode='html', reply_markup=main_keyboard())


@bot.message_handler(commands=['purpose'])
def purpose(message):
    text = 'I was made with the purpose of helping people learn more about bots and also provide a easier '
    bot.send_message(chat_id=message.chat.id, text=text, reply_markup=main_keyboard())


@bot.message_handler(commands=['dev'])
def dev(message):
    text = 'This is made with ❤ by <a href="https://github.com/themagicalmammal">@themagicalmammal</a>.\n If you ' \
           'require assistance or want me to update the bot, ' \
           'Please feel free to contact me. '
    bot.send_message(chat_id=message.chat.id, text=text, parse_mode='html', reply_markup=main_keyboard())


@bot.message_handler(commands=['source'])
def dev(message):
    text = 'Source Code for <a href="https://github.com/themagicalmammal/WikiBot">Wiki Bot</a>.'
    bot.send_message(chat_id=message.chat.id, text=text, parse_mode='html', reply_markup=main_keyboard())


@bot.message_handler(commands=['help'])
def aid(message):
    text = 'You can use the following commands: \n\n' \
           '<b>Primary</b> \n' \
           '/definition - fetches definition of the word you want \n' \
           '/title - fetches a bunch of related titles for a word \n' \
           '/url - gives the URL for the wiki page of the word \n' \
           '/lang - set the language you want (<a ' \
           'href="https://meta.wikimedia.org/wiki/List_of_Wikipedias">languages</a>) \n \n' \
           '<b>Secondary</b> \n' \
           '/map - location in map with wiki database \n' \
           '/random - fetches a random title from the wiki page \n' \
           '/suggest - returns a suggestion or none if not found \n\n' \
           '<b>Others</b> \n' \
           '/big - bigger version of definition & title \n' \
           '/extra - some extra set of commands'
    bot.send_message(chat_id=message.chat.id, text=text, parse_mode='html', reply_markup=main_keyboard())


@bot.message_handler(commands=['title'])
def title(message):
    title_msg = bot.reply_to(message, "Title" + word)
    bot.register_next_step_handler(title_msg, process_title)


def process_title(message):
    # noinspection PyBroadException
    try:
        title_msg = str(message.text)
        title_result = wikipedia.search(title_msg, results=4)
        for i in title_result:
            bot.send_message(chat_id=message.chat.id, text=i, reply_markup=main_keyboard())
    except Exception:
        bot.send_message(chat_id=message.chat.id, text=error, reply_markup=main_keyboard())


@bot.message_handler(commands=['titles'])
def titles(message):
    titles_msg = bot.reply_to(message, "Title" + word)
    bot.register_next_step_handler(titles_msg, process_titles)


def process_titles(message):
    # noinspection PyBroadException
    try:
        titles_msg = str(message.text)
        titles_result = wikipedia.search(titles_msg, sentences=100, suggestion=True)
        for i in titles_result:
            bot.send_message(chat_id=message.chat.id, text=i, parse_mode='html', reply_markup=main_keyboard())
    except Exception:
        bot.send_message(chat_id=message.chat.id, text=error, reply_markup=main_keyboard())


@bot.message_handler(commands=['url'])
def url(message):
    url_msg = bot.reply_to(message, "URL" + word)
    bot.register_next_step_handler(url_msg, process_url)


def process_url(message):
    # noinspection PyBroadException
    try:
        url_message = str(message.text)
        url_str = wikipedia.page(url_message)
        url_result = str(url_str.url)
        bot.send_message(chat_id=message.chat.id, text=url_result, reply_markup=main_keyboard())
    except Exception:
        bot.send_message(chat_id=message.chat.id, text=error, reply_markup=main_keyboard())


@bot.message_handler(commands=['random'])
def random(message):
    # noinspection PyBroadException
    try:
        random_title = str(wikipedia.random(pages=1))
        bot.send_message(chat_id=message.chat.id, text=random_title, reply_markup=main_keyboard())
    except Exception:
        bot.send_message(chat_id=message.chat.id, text=error, reply_markup=main_keyboard())


@bot.message_handler(commands=['definition'])
def definition(message):
    def_msg = bot.reply_to(message, "Definition" + word)
    bot.register_next_step_handler(def_msg, process_definition)


def process_definition(message):
    try:
        def_msg = str(message.text)
        def_str = str(wikipedia.summary(def_msg, sentences=20, auto_suggest=True, redirect=True))
        bot.send_message(chat_id=message.chat.id, text=def_str, reply_markup=main_keyboard())
    except Exception as c:
        bot.send_message(chat_id=message.chat.id, text=c, reply_markup=definition(message))


@bot.message_handler(commands=['definitions'])
def definitions(message):
    def_msgs = bot.reply_to(message, "Definition" + word)
    bot.register_next_step_handler(def_msgs, process_definitions)


def process_definitions(message):
    try:
        def_msgs = str(message.text)
        def_str = str(wikipedia.summary(def_msgs, auto_suggest=True, redirect=True))
        bot.send_message(chat_id=message.chat.id, text=def_str, reply_markup=main_keyboard())
    except Exception as c:
        bot.send_message(chat_id=message.chat.id, text=c, reply_markup=definition(message))


@bot.message_handler(commands=['map'])
def map(message):
    co_msg = bot.reply_to(message, "Location of the place...")
    bot.register_next_step_handler(co_msg, process_co)


def process_co(message):
    # noinspection PyBroadException
    try:
        co_msg = str(message.text)
        lat, lon = wikipedia.WikipediaPage(co_msg).coordinates
        bot.send_location(chat_id=message.chat.id, latitude=lat, longitude=lon, reply_markup=main_keyboard())
    except Exception:
        bot.send_message(chat_id=message.chat.id, text="Not a location.", reply_markup=main_keyboard())


@bot.message_handler(commands=['suggest'])
def suggest(message):
    suggest_msg = bot.reply_to(message, "You want suggestion for...")
    bot.register_next_step_handler(suggest_msg, process_suggest)


def process_suggest(message):
    # noinspection PyBroadException
    try:
        suggest_msg = str(message.text)
        suggest_str = str(wikipedia.suggest(suggest_msg))
        bot.send_message(chat_id=message.chat.id, text=suggest_str, reply_markup=main_keyboard())
    except Exception:
        bot.send_message(chat_id=message.chat.id, text="No Suggestions", reply_markup=definition(message))


@bot.message_handler(commands=['back'])
def back(message):
    bot.send_message(chat_id=message.chat.id, text="Going Back...", reply_markup=main_keyboard())


@bot.message_handler(commands=['lang'])
def ln(message):
    ln_msg = bot.reply_to(message, "Type the prefix of you language...")
    bot.register_next_step_handler(ln_msg, process_ln)


def process_ln(message):
    # noinspection PyBroadException
    try:
        ln_msg = str(message.text)
        ln_str = str(wikipedia.set_lang(ln_msg))
        if ln_str == "None":
            ln_str = "Done"
        bot.send_message(chat_id=message.chat.id, text=ln_str, reply_markup=main_keyboard())
    except Exception:
        bot.send_message(chat_id=message.chat.id, text="Error, setting language", reply_markup=definition(message))


def main_extra():
    markup = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True)
    texts = ['/purpose', '/dev', '/source', '/back']
    buttons = []
    for text in texts:
        button = types.KeyboardButton(text)
        buttons.append(button)
    markup.add(*buttons)
    return markup


def main_keyboard():
    markup = types.ReplyKeyboardMarkup(row_width=4, one_time_keyboard=True)
    texts = ['/definition', '/title', '/url', '/lang', '/map', '/random', '/suggest', '/help', '/big', '/extra']
    buttons = []
    for text in texts:
        button = types.KeyboardButton(text)
        buttons.append(button)
    markup.add(*buttons)
    return markup


while True:
    # noinspection PyBroadException
    try:
        bot.enable_save_next_step_handlers(delay=2)
        bot.load_next_step_handlers()
        bot.polling()
    except Exception:
        time.sleep(5)
