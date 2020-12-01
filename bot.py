import wikipedia
from telebot import TeleBot, types

API_TOKEN = ''  # Paste your token API
bot = TeleBot(token=API_TOKEN)
error = 'Wrong word, use /title'
error2 = 'Wrong word, use /suggest'
word = " for the word..."
commands = ['start', 'extra', 'special', 'purpose', 'dev', 'purpose', 'source', 'issues', 'contributions', 'help',
            'title', 'titles', 'url', 'random', 'spot', 'definition', 'map', 'nearby', 'suggest', 'back', 'commands',
            'lang']


def find_command(msg):
    for text in msg:
        if '/' in text:
            return text


@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome = 'Greetings! Welcome, I am WikiBot.\nTo know how to control me type /help.'
    bot.send_message(chat_id=message.chat.id, text=welcome, reply_markup=main_keyboard())


@bot.message_handler(commands=['extra'])
def send_welcome(message):
    text = 'A bunch of <b>extra commands</b> I provide: \n\n' \
           '/dev - provides information about my creator\n' \
           '/source - my source code\n' \
           '/contributions - to contribute to this project\n' \
           '/issues - to submit problems/issues\n' \
           '/purpose - shows the purpose why I was made'
    bot.send_message(chat_id=message.chat.id, text=text, parse_mode='html', reply_markup=main_extra())


@bot.message_handler(commands=['special'])
def send_welcome(message):
    text = 'Some <b>similar commands</b> I provide: \n\n' \
           '/suggest - returns a suggested word or none if not found \n' \
           '/titles - fetches all possible titles for a word\n' \
           '/spot - fetches a random title from the wiki page'
    bot.send_message(chat_id=message.chat.id, text=text, parse_mode='html', reply_markup=main_special())


@bot.message_handler(commands=['purpose'])
def purpose(message):
    text = 'I was made with the purpose to make wikipedia accessible with a bot.'
    bot.send_message(chat_id=message.chat.id, text=text, reply_markup=main_keyboard())


@bot.message_handler(commands=['dev'])
def dev(message):
    text = 'I was made with ❤ by @themagicalmammal.'
    bot.send_message(chat_id=message.chat.id, text=text, reply_markup=main_keyboard())


@bot.message_handler(commands=['source'])
def dev(message):
    text = 'This is an Open Source Project. My code is ' \
           '<a href="https://github.com/themagicalmammal/WikiBot">here</a>. '
    bot.send_message(chat_id=message.chat.id, text=text, parse_mode='html', reply_markup=main_keyboard())


@bot.message_handler(commands=['issues'])
def dev(message):
    text = 'If you have problems or want to submit a issue, go <a ' \
           'href="https://github.com/themagicalmammal/WikiBot/issues">here</a>. '
    bot.send_message(chat_id=message.chat.id, text=text, parse_mode='html', reply_markup=main_keyboard())


@bot.message_handler(commands=['contributions'])
def dev(message):
    text = 'href="https://github.com/themagicalmammal/WikiBot/pulls">Contributions</a> are happily accepted.'
    bot.send_message(chat_id=message.chat.id, text=text, parse_mode='html', reply_markup=main_keyboard())


@bot.message_handler(commands=['help'])
def aid(message):
    text = 'You can use the following commands: \n\n' \
           '<b>Primary</b> \n' \
           '/definition - fetches definition of the word you want \n' \
           '/title - fetches a bunch of related titles for a word \n' \
           '/url - gives the URL for the wiki page of the word \n' \
           '/lang - set the language you want, by typing its <a ' \
           'href="https://meta.wikimedia.org/wiki/List_of_Wikipedias">prefix</a> \n\n' \
           '<b>Secondary</b> \n' \
           '/map - location in map with wiki database \n' \
           '/nearby - locations near a coordinate \n' \
           '/random - pops a random article from wiki \n\n' \
           '<b>Others</b> \n' \
           '/special - some different set of commands \n' \
           '/extra - some extra set of commands \n\n' \
           "<b>Note:</b> If the commands don't show up type /commands\n"
    bot.send_message(chat_id=message.chat.id, text=text, parse_mode='html', reply_markup=main_keyboard())


@bot.message_handler(commands=['title'])
def title(message):
    title_msg = bot.reply_to(message, "<b>Title</b>" + word, parse_mode='html')
    bot.register_next_step_handler(title_msg, process_title)


def process_title(message):
    # noinspection PyBroadException
    try:
        title_msg = str(message.text)
        title_result = wikipedia.search(title_msg, results=4)
        if title_result:
            bot.send_message(chat_id=message.chat.id, text="Possible titles are...",
                             parse_mode='html')
            for i in title_result:
                bot.send_message(chat_id=message.chat.id, text=i.replace(title_msg, "<b>" + title_msg + "</b>")
                                 .replace(title_msg.lower(), "<b>" + title_msg.lower() + "</b>"),
                                 parse_mode='html', reply_markup=main_keyboard())
        else:
            bot.send_message(chat_id=message.chat.id, text=error2, reply_markup=main_keyboard())
    except Exception:
        bot.send_message(chat_id=message.chat.id, text=error2, reply_markup=main_keyboard())


@bot.message_handler(commands=['titles'])
def titles(message):
    titles_msg = bot.reply_to(message, "<b>Titles</b>" + word, parse_mode='html')
    bot.register_next_step_handler(titles_msg, process_titles)


def process_titles(message):
    # noinspection PyBroadException
    try:
        titles_msg = str(message.text)
        titles_result = wikipedia.search(titles_msg)
        bot.send_message(chat_id=message.chat.id, text="All possible titles are...",
                         parse_mode='html')
        if titles_result:
            for i in titles_result:
                bot.send_message(chat_id=message.chat.id, text=i.replace(titles_msg, "<b>" + titles_msg + "</b>")
                                 .replace(titles_msg.lower(), "<b>" + titles_msg.lower() + "</b>"),
                                 parse_mode='html', reply_markup=main_keyboard())
        else:
            bot.send_message(chat_id=message.chat.id, text=error2, reply_markup=main_keyboard())
    except Exception:
        bot.send_message(chat_id=message.chat.id, text=error2, reply_markup=main_keyboard())


@bot.message_handler(commands=['url'])
def url(message):
    url_msg = bot.reply_to(message, "<b>URL</b>" + word, parse_mode='html')
    bot.register_next_step_handler(url_msg, process_url)


def process_url(message):
    # noinspection PyBroadException
    try:
        url_message = str(message.text)
        url_str = wikipedia.page(url_message)
        url_result = str(url_str.url)
        pre = "URL for the word <b>" + url_message + "</b> is \n\n"
        bot.send_message(chat_id=message.chat.id, text=pre + url_result, parse_mode='html',
                         reply_markup=main_keyboard())
    except Exception:
        bot.send_message(chat_id=message.chat.id, text=error, reply_markup=main_keyboard())


@bot.message_handler(commands=['random'])
def random(message):
    # noinspection PyBroadException
    try:
        random_title = str(wikipedia.random(pages=1))
        random_page = wikipedia.page(random_title)
        random_result = str(random_page.url)
        bot.send_message(chat_id=message.chat.id, text=random_result, reply_markup=main_keyboard())
    except Exception:
        bot.send_message(chat_id=message.chat.id, text=error, reply_markup=main_keyboard())


@bot.message_handler(commands=['spot'])
def spot(message):
    # noinspection PyBroadException
    try:
        spot_title = str(wikipedia.random(pages=1))
        bot.send_message(chat_id=message.chat.id, text=spot_title, reply_markup=main_keyboard())
    except Exception:
        bot.send_message(chat_id=message.chat.id, text=error, reply_markup=main_keyboard())


@bot.message_handler(commands=['definition'])
def definition(message):
    def_msg = bot.reply_to(message, "<b>Definition</b>" + word, parse_mode='html')
    bot.register_next_step_handler(def_msg, process_definition)


def process_definition(message):
    try:
        def_msg = str(message.text)
        def_str = str(wikipedia.summary(def_msg, sentences=20, auto_suggest=True, redirect=True))
        bot.send_message(chat_id=message.chat.id, text="<b>" + def_msg + "</b> \n\n" + def_str, parse_mode='html',
                         reply_markup=main_keyboard())
    except Exception as c:
        msg = '<b>Multiple similar titles found!</b> \n\n'
        bot.send_message(chat_id=message.chat.id, text=msg + str(c), parse_mode='html', reply_markup=main_keyboard())


@bot.message_handler(commands=['map'])
def map(message):
    co_msg = bot.reply_to(message, "<b>Location</b> of the place...", parse_mode='html')
    bot.register_next_step_handler(co_msg, process_co)


def process_co(message):
    # noinspection PyBroadException
    try:
        co_msg = str(message.text)
        lat, lon = wikipedia.WikipediaPage(co_msg).coordinates
        bot.send_location(chat_id=message.chat.id, latitude=lat, longitude=lon, reply_markup=main_keyboard())
    except Exception:
        bot.send_message(chat_id=message.chat.id, text="Not a location.", reply_markup=main_keyboard())


@bot.message_handler(commands=['nearby'])
def geo(message):
    geo_msg = bot.reply_to(message, "Send me the <b>coordinates</b>...", parse_mode='html')
    bot.register_next_step_handler(geo_msg, process_geo)


def process_geo(message):
    # noinspection PyBroadException
    try:
        lat, lan = (str(message.text).replace('E', '').replace('W', '').replace('N', '').replace('S', '').
                    replace('° ', '').replace('°', '').replace(',', '').replace('  ', ' ').split(" "))
        for i in wikipedia.geosearch(latitude=lat, longitude=lan, results=5, radius=1000):
            bot.send_message(chat_id=message.chat.id, text=i, reply_markup=main_keyboard())
    except Exception:
        bot.send_message(chat_id=message.chat.id, text="Not a location.", reply_markup=main_keyboard())


@bot.message_handler(commands=['suggest'])
def suggest(message):
    suggest_msg = bot.reply_to(message, "You want <b>suggestion</b> for...", parse_mode='html')
    bot.register_next_step_handler(suggest_msg, process_suggest)


def process_suggest(message):
    # noinspection PyBroadException
    sorry = "Sorry, <b>no suggestions.</b>"
    try:
        suggest_msg = str(message.text)
        suggest_str = str(wikipedia.suggest(suggest_msg))
        if suggest_str != "None":
            pre = "Suggestion for the word <b>" + suggest_msg + "</b> is "
            bot.send_message(chat_id=message.chat.id, text=pre + suggest_str, parse_mode='html',
                             reply_markup=main_keyboard())
        else:
            bot.send_message(chat_id=message.chat.id, text=sorry, parse_mode='html', reply_markup=main_keyboard())
    except Exception:
        bot.send_message(chat_id=message.chat.id, text=sorry, parse_mode='html', reply_markup=main_keyboard())


@bot.message_handler(commands=['back'])
def back(message):
    bot.send_message(chat_id=message.chat.id, text="Going <b>Back</b>...", parse_mode='html',
                     reply_markup=main_keyboard())


@bot.message_handler(commands=['commands'])
def back(message):
    bot.send_message(chat_id=message.chat.id, text="<b>Commands</b>", parse_mode='html',
                     reply_markup=main_keyboard())


@bot.message_handler(commands=['lang'])
def ln(message):
    ln_msg = bot.reply_to(message, "Type the prefix of your <b>language</b>...", parse_mode='html')
    bot.register_next_step_handler(ln_msg, process_ln)


def process_ln(message):
    # noinspection PyBroadException
    try:
        ln_msg = str(message.text).lower()
        lang_list = ['aa', 'ab', 'abs', 'ace', 'ady', 'ady-cyrl', 'aeb', 'aeb-arab', 'aeb-latn', 'af', 'ak', 'aln',
                     'als', 'alt', 'am', 'ami', 'an', 'ang', 'anp', 'ar', 'arc', 'arn', 'arq', 'ary', 'arz', 'as',
                     'ase', 'ast', 'atj', 'av', 'avk', 'awa', 'ay', 'az', 'azb', 'ba', 'ban', 'ban-bali', 'bar',
                     'bat-smg', 'bbc', 'bbc-latn', 'bcc', 'bcl', 'be', 'be-tarask', 'be-x-old', 'bg', 'bgn', 'bh',
                     'bho', 'bi', 'bjn', 'bm', 'bn', 'bo', 'bpy', 'bqi', 'br', 'brh', 'bs', 'btm', 'bto', 'bug', 'bxr',
                     'ca', 'cbk-zam', 'cdo', 'ce', 'ceb', 'ch', 'cho', 'chr', 'chy', 'ckb', 'co', 'cps', 'cr', 'crh',
                     'crh-cyrl', 'crh-latn', 'cs', 'csb', 'cu', 'cv', 'cy', 'da', 'de', 'de-at', 'de-ch', 'de-formal',
                     'din', 'diq', 'dsb', 'dtp', 'dty', 'dv', 'dz', 'ee', 'egl', 'el', 'eml', 'en', 'en-ca', 'en-gb',
                     'eo', 'es', 'es-419', 'es-formal', 'et', 'eu', 'ext', 'fa', 'ff', 'fi', 'fit', 'fiu-vro', 'fj',
                     'fo', 'fr', 'frc', 'frp', 'frr', 'fur', 'fy', 'ga', 'gag', 'gan', 'gan-hans', 'gan-hant', 'gcr',
                     'gd', 'gl', 'glk', 'gn', 'gom', 'gom-deva', 'gom-latn', 'gor', 'got', 'grc', 'gsw', 'gu', 'gv',
                     'ha', 'hak', 'haw', 'he', 'hi', 'hif', 'hif-latn', 'hil', 'ho', 'hr', 'hrx', 'hsb', 'ht', 'hu',
                     'hu-formal', 'hy', 'hyw', 'hz', 'ia', 'id', 'ie', 'ig', 'ii', 'ik', 'ike-cans', 'ike-latn', 'ilo',
                     'inh', 'io', 'is', 'it', 'iu', 'ja', 'jam', 'jbo', 'jut', 'jv', 'ka', 'kaa', 'kab', 'kbd',
                     'kbd-cyrl', 'kbp', 'kg', 'khw', 'ki', 'kiu', 'kj', 'kjp', 'kk', 'kk-arab', 'kk-cn', 'kk-cyrl',
                     'kk-kz', 'kk-latn', 'kk-tr', 'kl', 'km', 'kn', 'ko', 'ko-kp', 'koi', 'kr', 'krc', 'kri', 'krj',
                     'krl', 'ks', 'ks-arab', 'ks-deva', 'ksh', 'ku', 'ku-arab', 'ku-latn', 'kum', 'kv', 'kw', 'ky',
                     'la', 'lad', 'lb', 'lbe', 'lez', 'lfn', 'lg', 'li', 'lij', 'liv', 'lki', 'lld', 'lmo', 'ln', 'lo',
                     'loz', 'lrc', 'lt', 'ltg', 'lus', 'luz', 'lv', 'lzh', 'lzz', 'mad', 'mai', 'map-bms', 'mdf', 'mg',
                     'mh', 'mhr', 'mi', 'min', 'mk', 'ml', 'mn', 'mni', 'mnw', 'mo', 'mr', 'mrh', 'mrj', 'ms', 'mt',
                     'mus', 'mwl', 'my', 'myv', 'mzn', 'na', 'nah', 'nan', 'nap', 'nb', 'nds', 'nds-nl', 'ne', 'new',
                     'ng', 'nia', 'niu', 'nl', 'nl-informal', 'nn', 'no', 'nov', 'nqo', 'nrm', 'nso', 'nv', 'ny', 'nys',
                     'oc', 'olo', 'om', 'or', 'os', 'pa', 'pag', 'pam', 'pap', 'pcd', 'pdc', 'pdt', 'pfl', 'pi', 'pih',
                     'pl', 'pms', 'pnb', 'pnt', 'prg', 'ps', 'pt', 'pt-br', 'qu', 'qug', 'rgn', 'rif', 'rm', 'rmy',
                     'rn', 'ro', 'roa-rup', 'roa-tara', 'ru', 'rue', 'rup', 'ruq', 'ruq-cyrl', 'ruq-latn', 'rw', 'sa',
                     'sah', 'sat', 'sc', 'scn', 'sco', 'sd', 'sdc', 'sdh', 'se', 'sei', 'ses', 'sg', 'sgs', 'sh', 'shi',
                     'shi-latn', 'shi-tfng', 'shn', 'shy-latn', 'si', 'simple', 'sk', 'skr', 'skr-arab', 'sl', 'sli',
                     'sm', 'sma', 'smn', 'sn', 'so', 'sq', 'sr', 'sr-ec', 'sr-el', 'srn', 'ss', 'st', 'stq', 'sty',
                     'su', 'sv', 'sw', 'szl', 'szy', 'ta', 'tay', 'tcy', 'te', 'tet', 'tg', 'tg-cyrl', 'tg-latn', 'th',
                     'ti', 'tk', 'tl', 'tly', 'tn', 'to', 'tpi', 'tr', 'tru', 'trv', 'ts', 'tt', 'tt-cyrl', 'tt-latn',
                     'tum', 'tw', 'ty', 'tyv', 'tzm', 'udm', 'ug', 'ug-arab', 'ug-latn', 'uk', 'ur', 'uz', 'uz-cyrl',
                     'uz-latn', 've', 'vec', 'vep', 'vi', 'vls', 'vmf', 'vo', 'vot', 'vro', 'wa', 'war', 'wo', 'wuu',
                     'xal', 'xh', 'xmf', 'xsy', 'yi', 'yo', 'yue', 'za', 'zea', 'zgh', 'zh', 'zh-classical', 'zh-cn',
                     'zh-hans', 'zh-hant', 'zh-hk', 'zh-min-nan', 'zh-mo', 'zh-my', 'zh-sg', 'zh-tw', 'zh-yue', 'zu']
        if ln_msg in lang_list:
            wikipedia.set_lang(ln_msg)
            bot.send_message(chat_id=message.chat.id, text="Done", reply_markup=main_keyboard())
        else:
            wrong = 'Wrong language, please check correct <a ' \
                    'href="https://meta.wikimedia.org/wiki/List_of_Wikipedias">prefix</a> '
            bot.send_message(chat_id=message.chat.id, text=wrong, parse_mode='html', reply_markup=main_keyboard())
    except Exception:
        bot.send_message(chat_id=message.chat.id, text="Error, setting language", reply_markup=main_keyboard())


def main_extra():
    markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True, one_time_keyboard=True)
    texts = ['/dev', '/source', '/contributions', '/issues', '/purpose', '/back']
    buttons = []
    for text in texts:
        button = types.KeyboardButton(text)
        buttons.append(button)
    markup.add(*buttons)
    return markup


def main_special():
    markup = types.ReplyKeyboardMarkup(row_width=4, resize_keyboard=True, one_time_keyboard=True)
    texts = ['/suggest', '/titles', '/spot', '/back']
    buttons = []
    for text in texts:
        button = types.KeyboardButton(text)
        buttons.append(button)
    markup.add(*buttons)
    return markup


def main_keyboard():
    markup = types.ReplyKeyboardMarkup(row_width=5, resize_keyboard=True, one_time_keyboard=True)
    texts = ['/definition', '/title', '/url', '/map', '/nearby', '/random', '/special', '/help', '/extra', '/lang']
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
        bot.reply_to(message, "Unrecognized command. Say whaaaat?")
    else:
        bot.reply_to(message, "You have to use /commands.")


bot.polling()
