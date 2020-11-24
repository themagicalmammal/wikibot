import time
import telebot
import wikipedia

bot_token = '1368302801:AAFfDg_C57Rl1BksQMZz4bNdUCkgjLwwKZ4'  # Paste the Token API
bot = telebot.TeleBot(token=bot_token)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Greetings! Welcome I am WikiBot.")
    time.sleep(5)
    bot.reply_to(message, "If you want some help, type /help.")


@bot.message_handler(commands=['purpose'])
def send_welcome(message):
    bot.reply_to(message, "This is a very simple bot, made with the purpose of helping people learn more about bots "
                          "and a provide as a general idea about how a bot should look.")


@bot.message_handler(commands=['dev'])
def send_welcome(message):
    bot.reply_to(message, "This is made with ❤ by @themagicalmammal.")
    bot.reply_to(message, "If you require assistance or want me to update the bot, Please feel free to contact me.")


@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "Type /how2use to know how it works.")
    bot.reply_to(message, "To know about the developer, type /dev.")


@bot.message_handler(commands=['how2use'])
def send_welcome(message):
    bot.reply_to(message, "/definition - to fetch definition of the word you typed.")
    bot.reply_to(message, "/title - sends you the title by cross checking it on wiki's database.")
    bot.reply_to(message, "/url - gives the url for the wiki page of the word you typed.")


@bot.message_handler(commands=['title'])
def send_welcome(message):
    msg = bot.reply_to(message, "The title should for the word....")
    bot.register_next_step_handler(msg, process_title_step)


def process_title_step(message):
    try:
        namer = str(message.text)
        nyr = wikipedia.search(namer)
        bot.reply_to(message, nyr)
    except Exception as e:
        bot.reply_to(message, 'Oops, Sorry')


@bot.message_handler(commands=['url'])
def send_welcome(message):
    msga = bot.reply_to(message, "You want URL for ....")
    bot.register_next_step_handler(msga, process_title_stepd)


def process_title_stepd(message):
    try:
        namef = str(message.text)
        nyf = wikipedia.page(namef)
        fdf = str(nyf.url)
        bot.reply_to(message, fdf)
    except Exception as e:
        bot.reply_to(message, 'Oops, Sorry')


@bot.message_handler(commands=['definition'])
def send_welcome(message):
    msgd = bot.reply_to(message, "Definition of the word....")
    bot.register_next_step_handler(msgd, process_title_stepe)


def process_title_stepe(message):
    try:
        namea = str(message.text)
        nya = wikipedia.page(namea)
        fda = str(nya.content)
        bot.reply_to(message, fda[0:2048])
    except Exception as e:
        bot.reply_to(message, 'Oops, Sorry')


while True:
    try:
        bot.enable_save_next_step_handlers(delay=2)
        bot.load_next_step_handlers()
        bot.polling()
    except Exception:
        time.sleep(15)

