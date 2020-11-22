import time
import telebot
import wikipedia

bot_token = ''#Paste the Token API
bot = telebot.TeleBot(token=bot_token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Greeting Sir! Welcome I am WikiBot")
    bot.reply_to(message, "If you dont know how to use type /howtouse.")


@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "Type /howtouse to know how it works")


@bot.message_handler(commands=['howtouse'])
def send_welcome(message):
    bot.reply_to(message, "Its very easy we have to commands.")
    bot.reply_to(message, "/Methods to know what methods I provide")
    bot.reply_to(message,
                 "/Typetheword this is not a direct command if you want to use it you can type any word after / and would work")


@bot.message_handler(commands=['Typetheword'])
def send_welcome(message):
    bot.reply_to(message, "Its not a method :( just mentioned it.")


@bot.message_handler(commands=['Methods'])
def send_welcome(message):
    bot.reply_to(message, "1. /title")
    bot.reply_to(message, "2. /url")
    bot.reply_to(message, "3. /definition")
    bot.reply_to(message, "If you need help with anything and want to know what actually the thing does just type /help(method)")
    bot.reply_to(message, " Example -  /helptitle")


@bot.message_handler(commands=['helptitle'])
def send_welcome(message):
    bot.reply_to(message, "send the title you just sent by cross checking it on wikidatabase")


@bot.message_handler(commands=['helpurl'])
def send_welcome(message):
    bot.reply_to(message, "gives the url of wiki page of the work you typed")


@bot.message_handler(commands=['helpdefinition'])
def send_welcome(message):
    bot.reply_to(message, "To fetch definition of the word I typed")


@bot.message_handler(commands=['title'])
def send_welcome(message):
    msg = bot.reply_to(message, "The title would be....")
    bot.register_next_step_handler(msg, process_title_step)


def process_title_step(message):
    try:
        namer = str(message.text)
        nyr = wikipedia.page(namer)
        fdr = str(nyr.title)
        bot.reply_to(message, fdr)
    except Exception as e:
        bot.reply_to(message, 'oooops')

@bot.message_handler(commands=['url'])
def send_welcome(message):
    msga = bot.reply_to(message, "The URL for title to open Wiki page is")
    bot.register_next_step_handler(msga, process_title_stepd)


def process_title_stepd(message):
    try:
        namef = str(message.text)
        nyf = wikipedia.page(namef)
        fdf = str(nyf.url)
        bot.reply_to(message, fdf)
    except Exception as e:
        bot.reply_to(message, 'oooops')


@bot.message_handler(commands=['definition'])
def send_welcome(message):
    msgd = bot.reply_to(message, "The Definition of the Word you want?")
    bot.register_next_step_handler(msgd, process_title_stepe)


def process_title_stepe(message):
    try:
        namea = str(message.text)
        nya = wikipedia.page(namea)
        fda = str(nya.content)
        bot.reply_to(message, fda[0:2048])
    except Exception as e:
        bot.reply_to(message, 'oooops')


while True:
    try:
        bot.enable_save_next_step_handlers(delay=2)
        bot.load_next_step_handlers()
        bot.polling()
    except Exception:
        time.sleep(15)
