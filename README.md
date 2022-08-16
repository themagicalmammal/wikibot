<p align="center">
 <a href="https://deepsource.io/gh/themagicalmammal/wikibot/?ref=repository-badge" target="_blank"><img alt="DeepSource" title="DeepSource" src="https://deepsource.io/gh/themagicalmammal/wikibot.svg/?label=active+issues&show_trend=true"/></a>
<a href="https://deepsource.io/gh/themagicalmammal/wikibot/?ref=repository-badge" target="_blank"><img alt="DeepSource" title="DeepSource" src="https://deepsource.io/gh/themagicalmammal/wikibot.svg/?label=resolved+issues&show_trend=true"/></a> <br >
<a href="https://github.com/themagicalmammal/wikibot"><img src="Resources/logo.gif" width='527'/></a> 
<br />
<a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-darkviolet"/></a>
<a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3+-darkviolet.svg"/></a>
<a href="https://github.com/themagicalmammal/wikibot/pulls"><img src="https://img.shields.io/badge/PRs-welcome-darkviolet.svg"/></a>
<a href="https://telegram.me/themagicalmammal"><img src="https://img.shields.io/badge/Support-active-darkviolet.svg"/></a>
<br />
<a href="https://lgtm.com/projects/g/themagicalmammal/wikibot/alerts/"><img src="https://img.shields.io/lgtm/alerts/g/themagicalmammal/wikibot.svg?logo=lgtm&logoWidth=18"/></a>
<a href="https://lgtm.com/projects/g/themagicalmammal/wikibot/context:python"><img alt="Language grade: Python" src="https://img.shields.io/lgtm/grade/python/g/themagicalmammal/wikibot.svg?logo=lgtm&logoWidth=18"/></a>
<br />
This :robot: is made in python with the help of the Wiki library.
<br /> <br />
<a href="https://flask.palletsprojects.com/en/1.1.x/"><img src="https://img.shields.io/badge/flask%20-%23000.svg?&style=for-the-badge&logo=flask&logoColor=white"/></a>
<a href="https://id.heroku.com/login"><img src="https://img.shields.io/badge/heroku%20-%23430098.svg?&style=for-the-badge&logo=heroku&logoColor=white"/></a>
<a href="https://firebase.google.com/"><img src="https://img.shields.io/badge/firebase%20-%23039BE5.svg?&style=for-the-badge&logo=firebase"/></a>
</p>

## Intro

While exploring bots, I discovered that there were no bot(s) that could do more than display the definition of a term. However, Wikipedia can do much more than simply display a definition. As a result, this bot was created solely to demonstrate what Wiki can do.  <br />

<p align="center">
<a href="https://telegram.me/pro_wikibot"><img src="References/info.png"/></a>
</p>

## Test

To test this bot. You can follow these steps:

1. Setup a Bot with **[BotFather](https://t.me/botfather)**.
1. Put your **Token** in

```python
TOKEN = ""
```

3. Setup **RTDB** in **[Firebase](https://firebase.google.com/)**.
1. Download your **key file**, place it next to your bot file

```python
cred = credentials.Certificate("xxxYOURKEYFILExxx.json")
```

5. Paste your RTDB url in

```python
firebase_admin.initialize_app(
    cred, {"databaseURL": "https://yourappname-user-default-rtdb.firebaseio.com/"}
)
```

6. Setup a project in **Heroku**.
1. Paste your Project url in

```python
bot.set_webhook(url="https://yourappname.herokuapp.com/" + TOKEN)
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

## Contributors

#### [kurkurzz](https://github.com/kurkurzz) - Introducing the keyboard & some optimized commands.
