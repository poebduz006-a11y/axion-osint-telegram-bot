# Axion OSINT Telegram Bot

Multi-module OSINT panel for Telegram (70+ public endpoints).

## Deploy on Render (24/7)

1. https://dashboard.render.com → New → Background Worker
2. Connect this GitHub repo
3. Build: `pip install -r requirements.txt`
4. Start: `python main.py`
5. Env: `TELEGRAM_TOKEN` = your BotFather token

Optional env: BRIX_API_KEY, SHODAN_KEY, HUNTER_KEY, NUMVERIFY_KEY, ABSTRACT_KEY, IPINFO_TOKEN, WHOISXML_KEY

## Local

```bash
export TELEGRAM_TOKEN=...
pip install -r requirements.txt
python main.py
```

## Commands

/start /panel /username /phone /email /ip /domain /breach /github /tg /name /full
