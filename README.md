<p align="center">
 <a href="https://deepsource.io/gh/themagicalmammal/Wikibot/?ref=repository-badge" target="_blank"><img alt="DeepSource" title="DeepSource" src="https://deepsource.io/gh/themagicalmammal/Wikibot.svg/?label=active+issues&show_trend=true"/></a>
<a href="https://deepsource.io/gh/themagicalmammal/Wikibot/?ref=repository-badge" target="_blank"><img alt="DeepSource" title="DeepSource" src="https://deepsource.io/gh/themagicalmammal/Wikibot.svg/?label=resolved+issues&show_trend=true"/></a> <br >
<a href="https://github.com/themagicalmammal/WikiBot"><img src="https://github.com/themagicalmammal/WikiBot/blob/master/Resources/logo.gif" width='527'/></a> 
<br />
<a href="https://github.com/themagicalmammal/WikiBot/blob/master/LICENSE"><img src="https://img.shields.io/badge/license-MIT-darkviolet"/></a>
<a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3-darkviolet.svg"/></a>
<a href="https://github.com/themagicalmammal/WikiBot/pulls"><img src="https://img.shields.io/badge/PRs-welcome-darkviolet.svg"/></a>
<a href="https://telegram.me/themagicalmammal"><img src="https://img.shields.io/badge/chat-on Telegram-darkviolet.svg"/></a>
<br />
Wikibot, a bot which uses the Wiki-library & provides you with features like definitions, titles & other cool stuff!
<br /> <br />
<a href="https://flask.palletsprojects.com/en/1.1.x/"><img src="https://img.shields.io/badge/flask%20-%23000.svg?&style=for-the-badge&logo=flask&logoColor=white"/></a>
<a href="https://id.heroku.com/login"><img src="https://img.shields.io/badge/heroku%20-%23430098.svg?&style=for-the-badge&logo=heroku&logoColor=white"/></a>
<a href="https://firebase.google.com/"><img src="https://img.shields.io/badge/firebase%20-%23039BE5.svg?&style=for-the-badge&logo=firebase"/></a>
</p>

### Table of Contents
* [Intro](#Intro)
* [Bot Commands](#bot-commands)
  * [Def](#1-def)
  * [Title](#2-title)
  * [URL](#3-url)
  * [Lang](#4-lang)
  * [Map](#5-map)
  * [Nearby](#6-nearby)
  * [Random](#7-random)
  * [Others](#8-others)
* [Test](#test)
* [Contribute](#contribute)
* [Credits](#credits)
* [References](#references)

## Intro
While researching about bots, I found out that, there existed no bot that could do more than showing the definition of a word. But, Wiki can do a lot more than just showing a definition. Thus, this bot was made with the sole purpose of showing what Wiki can do.  <br />
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

## Test
To test this bot. You can follow these steps:
1. Setup a Bot with **[BotFather](https://t.me/botfather)**.
2. Put your **Token** in
```python
TOKEN = ''
```
3. Setup **RTDB** in **[Firebase](https://firebase.google.com/)**.
4. Download your **key file**, place it next to your bot file
```python
cred = credentials.Certificate('xxxYOURKEYFILExxx.json')
```
5. Paste your RTDB url in 
```python
firebase_admin.initialize_app(cred, {'databaseURL': 'https://yourappname-user-default-rtdb.firebaseio.com/'})
```
6. Setup a project in **Heroku**.
7. Paste your Project url in
```python
bot.set_webhook(url='https://yourappname.herokuapp.com/' + TOKEN)
```
8. Files you need for Heroku
```heroku
xxxYOURKEYFILExxx.json #firebase key
Procfile
bot.py
requirements.txt
```
9. To resolve bugs
```heroku
Heroku --logs
```

## Contribute
Thank you for considering contributing to Wikibot. Please add useful comments with your PR's. <br /> <br />

To contact me go [here](https://telegram.me/themagicalmammal).

## Credits
#### [kurkurzz](https://github.com/kurkurzz) - Introducing the keyboard & some optimized commands.

## References
#### 1. [Webhook](https://github.com/eternnoir/pyTelegramBotAPI/tree/master/examples/webhook_examples) - To learn how to add a webhook to your bot.
#### 2. [Telebot](https://github.com/eternnoir/pyTelegramBotAPI/tree/master/examples) - Bot examples for texts & commands.
#### 3. [Firebase](https://www.youtube.com/watch?v=EiddkXBK0-o) - Easy way to learn about firebase.
#### 4. [Wiki-libs](https://wikipedia.readthedocs.io/en/latest/) - Simple docs to learn about its functions.
