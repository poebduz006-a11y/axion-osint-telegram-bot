#!/usr/bin/env python3
"""
Axion OSINT Telegram Bot
Repo: https://github.com/poebduz006-a11y/axion-osint-telegram-bot

On GitHub (phone):
1. Open this repo
2. Add file → Upload files
3. Upload axion-osint-telegram-bot-READY.py renamed to bot.py
4. Edit main.py to:

import runpy
runpy.run_path('bot.py', run_name='__main__')

Or replace this entire main.py with the READY file content.

Render: Background Worker, start command: python main.py
Env: TELEGRAM_TOKEN
"""
import os, sys
print('Upload bot.py (full READY file) then set main to run it.')
print('TELEGRAM_TOKEN set:', bool(os.environ.get('TELEGRAM_TOKEN')))
sys.exit(1)
