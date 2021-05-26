# Prerequisites
* python3.7

# Setup
* `python3.7 -m venv venv`
* `source venv/bin/activate`
* `pip install -r requirements.txt`
* create .env-file and add there variables `TG_BOT_KEY` and `CHAT_ID`

# Run
(from venv) `python server.py` -> open localhost:8000

# Hints
* name of test bot is yp_message_sender_bot, look for it in botfather chat 

# Helpers for webinar
* https://core.telegram.org/bots/api#available-methods
* `curl -XPOST https://api.telegram.org/bot.../getUpdates`
* `curl -XPOST https://api.telegram.org/bot.../sendMessage -d 'chat_id=...&text=Hello,world'`