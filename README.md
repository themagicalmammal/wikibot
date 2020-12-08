<p align="center">
<a href="https://github.com/themagicalmammal/WikiBot"><img src="https://github.com/themagicalmammal/WikiBot/blob/master/Resources/logo.gif" width='527'/></a> 
<br /><br />
<a href="https://github.com/themagicalmammal/WikiBot/blob/master/LICENSE"><img src="https://img.shields.io/badge/license-MIT-blueviolet"/></a>
<a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3-blueviolet.svg"/></a>
<a href="https://github.com/themagicalmammal/WikiBot/pulls"><img src="https://img.shields.io/badge/contributions-welcome-blueviolet.svg"/></a>
<a href="https://telegram.me/themagicalmammal"><img src="https://img.shields.io/badge/chat-on Telegram-blueviolet.svg"/></a>
<br />
Wikibot is a bot which with the help of wiki-library provides you with multiple features like definitions, titles, URLs & a lot more!
<br /> <br />
<a href="https://flask.palletsprojects.com/en/1.1.x/"><img src="https://img.shields.io/badge/flask%20-%23000.svg?&style=for-the-badge&logo=flask&logoColor=white"/></a>
<a href="https://id.heroku.com/login"><img src="https://img.shields.io/badge/heroku%20-%23430098.svg?&style=for-the-badge&logo=heroku&logoColor=white"/></a>
<a href="https://firebase.google.com/"><img src="https://img.shields.io/badge/firebase%20-%23039BE5.svg?&style=for-the-badge&logo=firebase"/></a>
</p>

## Table of Contents

* **[Bio](https://github.com/themagicalmammal/Wikibot#bio)**
* **[Bot Commands](https://github.com/themagicalmammal/Wikibot#bot-commands)**
  * [Def](https://github.com/themagicalmammal/Wikibot#1-def)
  * [Title](https://github.com/themagicalmammal/Wikibot#2-title)
  * [URL](https://github.com/themagicalmammal/Wikibot#3-url)
  * [Lang](https://github.com/themagicalmammal/Wikibot#4-lang)
  * [Map](https://github.com/themagicalmammal/Wikibot#5-map)
  * [Nearby](https://github.com/themagicalmammal/Wikibot#6-nearby)
  * [Random](https://github.com/themagicalmammal/Wikibot#7-random)
  * [Others](https://github.com/themagicalmammal/Wikibot#8-others)
* **[Try Out](https://github.com/themagicalmammal/Wikibot#try-out)**
* **[References](https://github.com/themagicalmammal/Wikibot#references)**
* **[Contribute](https://github.com/themagicalmammal/Wikibot#contribute)**
* **[Credits](https://github.com/themagicalmammal/Wikibot#credits)**
* **[License](https://github.com/themagicalmammal/Wikibot#license)**

## Bio
When I made this bot there existed no bot which did more than outputting the definition of a word. Wikipedia has a lot more set of functions that were not provided by any of the existing bots. So, this bot was made with the sole purpose of showing other functions that Wiki can provide. <br />
<p align="center">
<a href="https://telegram.me/pro_wikibot"><img src="https://github.com/themagicalmammal/WikiBot/blob/master/References/info.png"/></a>
</p>

## Bot Commands

### 1. Def
Short form of definition. Fetches wiki definition for your word.
```python
/def
```
<p align="center">
<a><img src="https://github.com/themagicalmammal/WikiBot/blob/master/References/def.gif"/></a>
</p>

### 2. Title
Shows a list of possible titles that you can search from a word.
```python
/title
```
<p align="center">
<a><img src="https://github.com/themagicalmammal/WikiBot/blob/master/References/title.gif"/></a>
</p>

### 3. URL
Provides you with the URL of the wiki page for a word.
```python
/url
```
<p align="center">
<a><img src="https://github.com/themagicalmammal/WikiBot/blob/master/References/url.gif"/></a>
</p>

### 4. Lang
Change to your local language which will be used for every wiki output.
```python
/lang
/prefix
```
<p align="center">
<a><img src="https://github.com/themagicalmammal/WikiBot/blob/master/References/lang.gif"/></a>
</p>

### 5. Map
Provides you with the location of your input place with Wiki-API.
```python
/map
```
<p align="center">
<a><img src="https://github.com/themagicalmammal/WikiBot/blob/master/References/map.gif"/></a>
</p>

### 6. Nearby
With the help of coordinates provides you with nearby locations under 1km.
```python
/nearby
```
<p align="center">
<a><img src="https://github.com/themagicalmammal/WikiBot/blob/master/References/nearby.gif"/></a>
</p>

### 7. Random
Sends you a random wiki link.
```python
/random
```
<p align="center">
<a><img src="https://github.com/themagicalmammal/WikiBot/blob/master/References/random.gif"/></a>
</p>

### 8. Others
Some other set of commands that wikibot provides.
```python
/help
/extra
/spot
/suggest
/dev
/source
/issues
```
<p align="center">
<a><img src="https://github.com/themagicalmammal/WikiBot/blob/master/References/other.gif"/></a>
</p>

## Try Out
If you want to test this with your bot. You can follow these **steps:**
1. Setup a **Bot** with **[BotFather](https://t.me/botfather)**.
2. Put your **Token** in
```python
TOKEN = ''
```
3. Setup **RTDB** in **[Firebase](https://firebase.google.com/)**.
4. Download your **key file**, then either you can modfiy below line or rename your key to firebase.json.
```python
cred = credentials.Certificate('firebase.json')
```
5. Place it next to bot.py.
6. Paste your RTDB link in 
```python
firebase_admin.initialize_app(cred, {'databaseURL': 'https://yourappname-user-default-rtdb.firebaseio.com/'})
```
7. Setup a Project in **Heroku**.
8. Paste your Project URL in
```python
bot.set_webhook(url='https://yourappname.herokuapp.com/' + TOKEN)
```
9. Files needed for Heroku
```heroku
firebase.json
Procfile
bot.py
requirements.txt
```
10. Done! Your project should run if not check **Heroku --logs**.

## References
#### 1. [Webhook](https://github.com/eternnoir/pyTelegramBotAPI/tree/master/examples/webhook_examples) - To learn how to add a webhook to your bot.
#### 2. [Telebot](https://github.com/eternnoir/pyTelegramBotAPI/tree/master/examples) - Bot examples for texts & commands.
#### 3. [Firebase](https://www.youtube.com/watch?v=EiddkXBK0-o) - Easy way to learn about firebase.
#### 4. [Wiki-libs](https://wikipedia.readthedocs.io/en/latest/) - Simple docs to learn about its functions.

## Contribute
Thank you for considering contributing to Wikibot. Please add useful comments or try contacting [me](https://telegram.me/themagicalmammal) before submitting any pull requests.

## Credits
#### [kurkurzz](https://github.com/kurkurzz) - Introducing the keyboard & some optimized commands.

## License
### The MIT License ([MIT](https://github.com/themagicalmammal/Wikibot/blob/master/LICENSE))
Copyright © 2020 Dipan
