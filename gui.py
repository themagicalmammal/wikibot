import time
from tkinter import *

import wikipedia
from telebot import TeleBot
from PIL import ImageTk, Image


root = Tk()
root.title("Wiki Bot")
root.geometry("450x250")
root.iconbitmap("bot.ico")

image = Image.open('logo.png')
image = image.resize((407, 183), Image.ANTIALIAS)
my_img = ImageTk.PhotoImage(image)
logo = Label(image=my_img)
logo.pack()
topFrame = Frame(root)
topFrame.pack()
label = Label(topFrame, text="Enter your Token API : ")
label.pack(side=LEFT)
e = Entry(topFrame, width=50, fg="#f44336")
e.pack(side=RIGHT)


def script(bot_token):
    bot = TeleBot(token=bot_token)

    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.reply_to(message, "Greetings! Welcome I am WikiBot.")
        time.sleep(5)
        bot.reply_to(message, "If you want some help, type /help.")

    @bot.message_handler(commands=['purpose'])
    def purpose(message):
        bot.reply_to(message,
                     "This is a very simple bot, made with the purpose of helping people learn more about bots "
                     "and a provide as a general idea about how a bot should look.")

    @bot.message_handler(commands=['dev'])
    def dev(message):
        bot.reply_to(message, "This is made with ❤ by @themagicalmammal.")
        bot.reply_to(message, "If you require assistance or want me to update the bot, Please feel free to contact me.")

    @bot.message_handler(commands=['help'])
    def aid(message):
        bot.reply_to(message, "Type /how2use to know how it works.")
        bot.reply_to(message, "To know about the developer, type /dev.")

    @bot.message_handler(commands=['how2use'])
    def utilize(message):
        bot.reply_to(message, "/definition - fetches definition of the word you typed.")
        bot.reply_to(message, "/title - fetches a bunch of possible titles for the word you send.")
        bot.reply_to(message, "/url - gives the url for the wiki page of the word you typed.")

    @bot.message_handler(commands=['title'])
    def title(message):
        title_msg = bot.reply_to(message, "The title should for the word....")
        bot.register_next_step_handler(title_msg, process_title)

    def process_title(message):
        try:
            title_message = str(message.text)
            title_result = wikipedia.search(title_message)
            for i in title_result:
                bot.reply_to(message, i)
        except Exception as e:
            bot.reply_to(message, 'Oops, Sorry')

    @bot.message_handler(commands=['url'])
    def url(message):
        url_msg = bot.reply_to(message, "You want URL for ....")
        bot.register_next_step_handler(url_msg, process_url)

    def process_url(message):
        try:
            url_message = str(message.text)
            url_string = wikipedia.page(url_message)
            url_result = str(url_string.url)
            bot.reply_to(message, url_result)
        except Exception as e:
            bot.reply_to(message, 'Oops, Sorry')

    @bot.message_handler(commands=['definition'])
    def definition(message):
        def_msg = bot.reply_to(message, "Definition of the word....")
        bot.register_next_step_handler(def_msg, process_definition)

    def process_definition(message):
        try:
            def_message = str(message.text)
            def_string = wikipedia.page(def_message)
            def_result = str(def_string.content)
            bot.reply_to(message, def_result[0:2048])
        except Exception as e:
            bot.reply_to(message, 'Oops, Sorry')

    while True:
        # noinspection PyBroadException
        try:
            bot.enable_save_next_step_handlers(delay=2)
            bot.load_next_step_handlers()
            bot.polling()
        except Exception:
            time.sleep(15)


def direct():
    key = e.get()
    if key != '':
        script(key)


bottomFrame = Frame(root)
bottomFrame.pack(side=RIGHT)
Run = Button(bottomFrame, text="Run", command=direct, bg="#1976D2", fg="white", padx=20, pady=4)
Run.pack(side=RIGHT)

root.mainloop()
