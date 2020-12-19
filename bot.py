import os
import wikipedia as wiki
from flask import Flask, request
from firebase_admin import initialize_app, credentials, db
from telebot import TeleBot, types

# Firebase connection
cred = credentials.Certificate("firebase.json")  # Firebase key
initialize_app(
    cred,
    {"databaseURL": "https://yourappname-user-default-rtdb.firebaseio.com/"})
ref = db.reference("/")
z = ref.get()

# Telegram API
TOKEN = ""  # Bot key
bot = TeleBot(TOKEN)

# Flask connection
server = Flask(__name__)

error = "Wrong word, use /title"
error2 = "Wrong word, use /suggest"
word = " for the word..."
commands = [
    "start",
    "extra",
    "dev",
    "source",
    "issues",
    "help",
    "title",
    "url",
    "random",
    "spot",
    "def",
    "map",
    "nearby",
    "suggest",
    "back",
    "commands",
    "lang",
]


def add_user(message):
    user_id = message.from_user.id
    ref.update({user_id: "en"})


def set_lan(message):
    user_id = message.from_user.id
    ref.update({user_id: message.text})
    global z
    z = ref.get()


def change_lan(message):
    user_id = str(message.from_user.id)
    wiki.set_lang(z[user_id])


def find_command(msg):
    for text in msg:
        if "/" in text:
            return text


@bot.message_handler(commands=["start"])
def welcome(message):
    add_user(message)
    first = message.from_user.first_name
    welcome = ("Greetings " + first +
               "! Welcome, I am Wikibot.\nTo learn how to control me, /help.")
    bot.send_message(chat_id=message.chat.id,
                     text=welcome,
                     reply_markup=main_keyboard())


@bot.message_handler(func=lambda message: True
if message.text.lower() in ["hi", "hey"] else False)
def command_text_hi(message):
    reply = message.text.lower().replace(
        "h", "H") + "! " + message.from_user.first_name
    bot.send_message(chat_id=message.chat.id, text=reply)


@bot.message_handler(commands=["extra"])
def extra(message):
    text = ("A bunch of <b>extra commands</b> I provide: \n\n"
            "/dev - provides information about my creator\n"
            "/source - my source code\n"
            "/issues - to submit problems/issues or suggest mods")
    bot.send_message(chat_id=message.chat.id,
                     text=text,
                     parse_mode="html",
                     reply_markup=main_extra())


@bot.message_handler(commands=["dev"])
def dev(message):
    text = "I was made with ❤ by @themagicalmammal."
    bot.send_message(chat_id=message.chat.id,
                     text=text,
                     reply_markup=main_keyboard())


@bot.message_handler(commands=["source"])
def source(message):
    text = ("This is a Open Source Project. To checkout my "
            '<a href="https://github.com/themagicalmammal/Wikibot">code</a>. ')
    bot.send_message(
        chat_id=message.chat.id,
        text=text,
        parse_mode="html",
        reply_markup=main_keyboard(),
    )


@bot.message_handler(commands=["issues"])
def issues(message):
    text = (
        "To submit a issue or suggest a useful revision, use <a "
        'href="https://github.com/themagicalmammal/Wikibot/issues">this</a>. ')
    bot.send_message(
        chat_id=message.chat.id,
        text=text,
        parse_mode="html",
        reply_markup=main_keyboard(),
    )


@bot.message_handler(commands=["prefix"])
def prefix(message):
    text = (
        "You can set your language with the help of prefix, for English it is en if you know your language "
        "prefix you can type it but if you need help you can use <a "
        "href='https://github.com/themagicalmammal/Wikibot/blob/master/Lang.md'>this</a>."
    )
    bot.send_message(
        chat_id=message.chat.id,
        text=text,
        parse_mode="html",
        reply_markup=main_keyboard(),
    )


@bot.message_handler(commands=["help"])
def aid(message):
    text = ("You can use the following commands: \n\n"
            "<b>Primary</b> \n"
            "/def - fetches definition of the word you want \n"
            "/title - fetches a bunch of related titles for a word \n"
            "/url - gives the URL for the wiki page of the word \n"
            "/lang - set the language you want (languages use /prefix) \n\n"
            "<b>Secondary</b> \n"
            "/map - location in map with wiki database \n"
            "/nearby - locations near a coordinate \n"
            "/random - pops a random article from wiki \n\n"
            "<b>Others</b> \n"
            "/suggest - returns a suggested word or none if not found \n"
            "/spot - fetches a random title from the wiki page \n"
            "/extra - some extra set of commands \n\n"
            "<b>Note:</b> If the commands don't show up type /commands\n")
    bot.send_message(
        chat_id=message.chat.id,
        text=text,
        parse_mode="html",
        reply_markup=main_keyboard(),
    )


@bot.message_handler(commands=["title"])
def title(message):
    title_msg = bot.reply_to(message, "<b>Title</b>" + word, parse_mode="html")
    bot.register_next_step_handler(title_msg, process_title)


def process_title(message):
    # noinspection PyBroadException
    try:
        title_msg = str(message.text)
        change_lan(message)
        title_result = wiki.search(title_msg)
        if title_result:
            bot.send_message(
                chat_id=message.chat.id,
                text="Possible titles are...",
                parse_mode="html",
            )
            for i in title_result:
                bot.send_message(
                    chat_id=message.chat.id,
                    text=i.replace(title_msg,
                                   "<b>" + title_msg + "</b>").replace(
                        title_msg.lower(),
                        "<b>" + title_msg.lower() + "</b>"),
                    parse_mode="html",
                    reply_markup=main_keyboard(),
                )
        else:
            bot.send_message(chat_id=message.chat.id,
                             text=error2,
                             reply_markup=main_keyboard())
    except Exception:
        bot.send_message(chat_id=message.chat.id,
                         text=error2,
                         reply_markup=main_keyboard())


@bot.message_handler(commands=["url"])
def url(message):
    url_msg = bot.reply_to(message, "<b>URL</b>" + word, parse_mode="html")
    bot.register_next_step_handler(url_msg, process_url)


def process_url(message):
    # noinspection PyBroadException
    try:
        url_message = str(message.text)
        change_lan(message)
        url_page = wiki.page(url_message)
        url_result = url_page.url
        pre = "URL for the word <b>" + url_message + "</b> is \n\n"
        bot.send_message(
            chat_id=message.chat.id,
            text=pre + url_result,
            parse_mode="html",
            reply_markup=main_keyboard(),
        )
    except Exception:
        bot.send_message(chat_id=message.chat.id,
                         text=error,
                         reply_markup=main_keyboard())


@bot.message_handler(commands=["random"])
def random(message):
    # noinspection PyBroadException
    try:
        change_lan(message)
        random_title = str(wiki.random(pages=1))
        random_page = wiki.page(random_title)
        random_result = random_page.url
        bot.send_message(chat_id=message.chat.id,
                         text=random_result,
                         reply_markup=main_keyboard())
    except Exception:
        bot.send_message(chat_id=message.chat.id,
                         text=error,
                         reply_markup=main_keyboard())


@bot.message_handler(commands=["spot"])
def spot(message):
    # noinspection PyBroadException
    try:
        change_lan(message)
        spot_title = str(wiki.random(pages=1))
        bot.send_message(chat_id=message.chat.id,
                         text=spot_title,
                         reply_markup=main_keyboard())
    except Exception:
        bot.send_message(chat_id=message.chat.id,
                         text=error,
                         reply_markup=main_keyboard())


@bot.message_handler(commands=["def"])
def definition(message):
    def_msg = bot.reply_to(message,
                           "<b>Definition</b>" + word,
                           parse_mode="html")
    bot.register_next_step_handler(def_msg, process_definition)


def process_definition(message):
    try:
        def_msg = str(message.text)
        change_lan(message)
        def_str = wiki.summary(def_msg, sentences=19)
        bot.send_message(
            chat_id=message.chat.id,
            text="<b>" + def_msg + "</b> \n\n" + def_str,
            parse_mode="html",
            reply_markup=main_keyboard(),
        )
    except Exception as c:
        if str(c)[:7] == "Page id":
            msg = "Not found"
        else:
            msg = "Multiple similar titles found"
        bot.send_message(
            chat_id=message.chat.id,
            text="<b>" + msg + "!</b> \n\n" + str(c),
            parse_mode="html",
            reply_markup=main_keyboard(),
        )


@bot.message_handler(commands=["map"])
def chart(message):
    co_msg = bot.reply_to(message,
                          "<b>Location</b> of the place...",
                          parse_mode="html")
    bot.register_next_step_handler(co_msg, process_co)


def process_co(message):
    # noinspection PyBroadException
    try:
        co_msg = str(message.text)
        wiki.set_lang("en")
        lat, lon = wiki.WikipediaPage(co_msg).coordinates
        bot.send_location(
            chat_id=message.chat.id,
            latitude=lat,
            longitude=lon,
            reply_markup=main_keyboard(),
        )
    except Exception:
        bot.send_message(
            chat_id=message.chat.id,
            text="Not a location.",
            reply_markup=main_keyboard(),
        )


@bot.message_handler(commands=["nearby"])
def geo(message):
    geo_msg = bot.reply_to(message,
                           "Send me the <b>coordinates</b>...",
                           parse_mode="html")
    bot.register_next_step_handler(geo_msg, process_geo)


def process_geo(message):
    # noinspection PyBroadException
    try:
        lat, lan = (str(message.text).replace("E", "").replace(
            "W",
            "").replace("N", "").replace("S", "").replace("° ", "").replace(
            "°", "").replace(",", "").replace("  ", " ").split(" "))
        wiki.set_lang("en")
        locations = wiki.geosearch(latitude=lat,
                                   longitude=lan,
                                   results=5,
                                   radius=1000)
        if locations:
            nearby = "<b>Nearby locations</b> I could find..."
            bot.send_message(
                chat_id=message.chat.id,
                text=nearby,
                parse_mode="html",
                reply_markup=main_keyboard(),
            )
            for i in locations:
                bot.send_message(chat_id=message.chat.id,
                                 text=i,
                                 reply_markup=main_keyboard())
        else:
            sorry = "Sorry, can't find nearby locations"
            bot.send_message(chat_id=message.chat.id,
                             text=sorry,
                             reply_markup=main_keyboard())
    except Exception:
        bot.send_message(
            chat_id=message.chat.id,
            text="Not a location.",
            reply_markup=main_keyboard(),
        )


@bot.message_handler(commands=["suggest"])
def suggest(message):
    suggest_msg = bot.reply_to(message,
                               "You want <b>suggestion</b> for...",
                               parse_mode="html")
    bot.register_next_step_handler(suggest_msg, process_suggest)


def process_suggest(message):
    sorry = "Sorry, <b>no suggestions.</b>"
    # noinspection PyBroadException
    try:
        suggest_msg = str(message.text)
        change_lan(message)
        suggest_str = str(wiki.suggest(suggest_msg))
        if suggest_str != "None":
            pre = "Suggestion for the word <b>" + suggest_msg + "</b> is "
            text = pre + suggest_str
        else:
            text = sorry
        bot.send_message(
            chat_id=message.chat.id,
            text=text,
            parse_mode="html",
            reply_markup=main_keyboard(),
        )
    except Exception:
        bot.send_message(
            chat_id=message.chat.id,
            text=sorry,
            parse_mode="html",
            reply_markup=main_keyboard(),
        )


@bot.message_handler(commands=["commands", "back"])
def back(message):
    bot.send_message(
        chat_id=message.chat.id,
        text="<b>Commands</b>",
        parse_mode="html",
        reply_markup=main_keyboard(),
    )


@bot.message_handler(commands=["lang"])
def ln(message):
    ln_msg = bot.reply_to(message,
                          "Type the prefix of your <b>language</b>...",
                          parse_mode="html")
    bot.register_next_step_handler(ln_msg, process_ln)


def process_ln(message):
    # noinspection PyBroadException
    try:
        ln_msg = str(message.text).lower()
        lang_list = [
            "aa",
            "ab",
            "abs",
            "ace",
            "ady",
            "ady-cyrl",
            "aeb",
            "aeb-arab",
            "aeb-latn",
            "af",
            "ak",
            "aln",
            "als",
            "alt",
            "am",
            "ami",
            "an",
            "ang",
            "anp",
            "ar",
            "arc",
            "arn",
            "arq",
            "ary",
            "arz",
            "as",
            "ase",
            "ast",
            "atj",
            "av",
            "avk",
            "awa",
            "ay",
            "az",
            "azb",
            "ba",
            "ban",
            "ban-bali",
            "bar",
            "bat-smg",
            "bbc",
            "bbc-latn",
            "bcc",
            "bcl",
            "be",
            "be-tarask",
            "be-x-old",
            "bg",
            "bgn",
            "bh",
            "bho",
            "bi",
            "bjn",
            "bm",
            "bn",
            "bo",
            "bpy",
            "bqi",
            "br",
            "brh",
            "bs",
            "btm",
            "bto",
            "bug",
            "bxr",
            "ca",
            "cbk-zam",
            "cdo",
            "ce",
            "ceb",
            "ch",
            "cho",
            "chr",
            "chy",
            "ckb",
            "co",
            "cps",
            "cr",
            "crh",
            "crh-cyrl",
            "crh-latn",
            "cs",
            "csb",
            "cu",
            "cv",
            "cy",
            "da",
            "de",
            "de-at",
            "de-ch",
            "de-formal",
            "din",
            "diq",
            "dsb",
            "dtp",
            "dty",
            "dv",
            "dz",
            "ee",
            "egl",
            "el",
            "eml",
            "en",
            "en-ca",
            "en-gb",
            "eo",
            "es",
            "es-419",
            "es-formal",
            "et",
            "eu",
            "ext",
            "fa",
            "ff",
            "fi",
            "fit",
            "fiu-vro",
            "fj",
            "fo",
            "fr",
            "frc",
            "frp",
            "frr",
            "fur",
            "fy",
            "ga",
            "gag",
            "gan",
            "gan-hans",
            "gan-hant",
            "gcr",
            "gd",
            "gl",
            "glk",
            "gn",
            "gom",
            "gom-deva",
            "gom-latn",
            "gor",
            "got",
            "grc",
            "gsw",
            "gu",
            "gv",
            "ha",
            "hak",
            "haw",
            "he",
            "hi",
            "hif",
            "hif-latn",
            "hil",
            "ho",
            "hr",
            "hrx",
            "hsb",
            "ht",
            "hu",
            "hu-formal",
            "hy",
            "hyw",
            "hz",
            "ia",
            "id",
            "ie",
            "ig",
            "ii",
            "ik",
            "ike-cans",
            "ike-latn",
            "ilo",
            "inh",
            "io",
            "is",
            "it",
            "iu",
            "ja",
            "jam",
            "jbo",
            "jut",
            "jv",
            "ka",
            "kaa",
            "kab",
            "kbd",
            "kbd-cyrl",
            "kbp",
            "kg",
            "khw",
            "ki",
            "kiu",
            "kj",
            "kjp",
            "kk",
            "kk-arab",
            "kk-cn",
            "kk-cyrl",
            "kk-kz",
            "kk-latn",
            "kk-tr",
            "kl",
            "km",
            "kn",
            "ko",
            "ko-kp",
            "koi",
            "kr",
            "krc",
            "kri",
            "krj",
            "krl",
            "ks",
            "ks-arab",
            "ks-deva",
            "ksh",
            "ku",
            "ku-arab",
            "ku-latn",
            "kum",
            "kv",
            "kw",
            "ky",
            "la",
            "lad",
            "lb",
            "lbe",
            "lez",
            "lfn",
            "lg",
            "li",
            "lij",
            "liv",
            "lki",
            "lld",
            "lmo",
            "ln",
            "lo",
            "loz",
            "lrc",
            "lt",
            "ltg",
            "lus",
            "luz",
            "lv",
            "lzh",
            "lzz",
            "mad",
            "mai",
            "map-bms",
            "mdf",
            "mg",
            "mh",
            "mhr",
            "mi",
            "min",
            "mk",
            "ml",
            "mn",
            "mni",
            "mnw",
            "mo",
            "mr",
            "mrh",
            "mrj",
            "ms",
            "mt",
            "mus",
            "mwl",
            "my",
            "myv",
            "mzn",
            "na",
            "nah",
            "nan",
            "nap",
            "nb",
            "nds",
            "nds-nl",
            "ne",
            "new",
            "ng",
            "nia",
            "niu",
            "nl",
            "nl-informal",
            "nn",
            "no",
            "nov",
            "nqo",
            "nrm",
            "nso",
            "nv",
            "ny",
            "nys",
            "oc",
            "olo",
            "om",
            "or",
            "os",
            "pa",
            "pag",
            "pam",
            "pap",
            "pcd",
            "pdc",
            "pdt",
            "pfl",
            "pi",
            "pih",
            "pl",
            "pms",
            "pnb",
            "pnt",
            "prg",
            "ps",
            "pt",
            "pt-br",
            "qu",
            "qug",
            "rgn",
            "rif",
            "rm",
            "rmy",
            "rn",
            "ro",
            "roa-rup",
            "roa-tara",
            "ru",
            "rue",
            "rup",
            "ruq",
            "ruq-cyrl",
            "ruq-latn",
            "rw",
            "sa",
            "sah",
            "sat",
            "sc",
            "scn",
            "sco",
            "sd",
            "sdc",
            "sdh",
            "se",
            "sei",
            "ses",
            "sg",
            "sgs",
            "sh",
            "shi",
            "shi-latn",
            "shi-tfng",
            "shn",
            "shy-latn",
            "si",
            "simple",
            "sk",
            "skr",
            "skr-arab",
            "sl",
            "sli",
            "sm",
            "sma",
            "smn",
            "sn",
            "so",
            "sq",
            "sr",
            "sr-ec",
            "sr-el",
            "srn",
            "ss",
            "st",
            "stq",
            "sty",
            "su",
            "sv",
            "sw",
            "szl",
            "szy",
            "ta",
            "tay",
            "tcy",
            "te",
            "tet",
            "tg",
            "tg-cyrl",
            "tg-latn",
            "th",
            "ti",
            "tk",
            "tl",
            "tly",
            "tn",
            "to",
            "tpi",
            "tr",
            "tru",
            "trv",
            "ts",
            "tt",
            "tt-cyrl",
            "tt-latn",
            "tum",
            "tw",
            "ty",
            "tyv",
            "tzm",
            "udm",
            "ug",
            "ug-arab",
            "ug-latn",
            "uk",
            "ur",
            "uz",
            "uz-cyrl",
            "uz-latn",
            "ve",
            "vec",
            "vep",
            "vi",
            "vls",
            "vmf",
            "vo",
            "vot",
            "vro",
            "wa",
            "war",
            "wo",
            "wuu",
            "xal",
            "xh",
            "xmf",
            "xsy",
            "yi",
            "yo",
            "yue",
            "za",
            "zea",
            "zgh",
            "zh",
            "zh-classical",
            "zh-cn",
            "zh-hans",
            "zh-hant",
            "zh-hk",
            "zh-min-nan",
            "zh-mo",
            "zh-my",
            "zh-sg",
            "zh-tw",
            "zh-yue",
            "zu",
        ]
        if ln_msg in lang_list:
            set_lan(ln_msg)
            text = "Language, set successfully."
        else:
            text = (
                "Wrong language, please check correct <a "
                'href="https://github.com/themagicalmammal/Wikibot/blob/master/Lang.md">prefix</a> '
            )
        bot.send_message(
            chat_id=message.chat.id,
            text=text,
            parse_mode="html",
            reply_markup=main_keyboard(),
        )
    except Exception:
        bot.send_message(
            chat_id=message.chat.id,
            text="Error, setting language",
            reply_markup=main_keyboard(),
        )


def main_extra():
    markup = types.ReplyKeyboardMarkup(row_width=2,
                                       resize_keyboard=True,
                                       one_time_keyboard=True)
    texts = ["/dev", "/source", "/issues", "/back"]
    buttons = []
    for text in texts:
        button = types.KeyboardButton(text)
        buttons.append(button)
    markup.add(*buttons)
    return markup


def main_keyboard():
    markup = types.ReplyKeyboardMarkup(row_width=3,
                                       resize_keyboard=True,
                                       one_time_keyboard=True)
    texts = [
        "/def",
        "/title",
        "/url",
        "/lang",
        "/map",
        "/nearby",
        "/random",
        "/help",
        "/extra",
    ]
    buttons = []
    for text in texts:
        button = types.KeyboardButton(text)
        buttons.append(button)
    markup.add(*buttons)
    return markup


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    check = find_command(message.text.split())
    if check:
        if check[1:] in commands:
            msg = "Wrong usage of command"
        else:
            msg = "Unrecognized command. Say What?"
    else:
        msg = "You have to use /commands."
    bot.reply_to(message, msg)


# Heroku Connection
@server.route("/" + TOKEN, methods=["POST"])
def establish():
    bot.process_new_updates(
        [types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url="https://yourappname.herokuapp.com/" + TOKEN)
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
