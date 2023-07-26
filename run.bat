@echo off

call %~dp0Bot\venv\Scripts\activate

cd %~dp0Bot

set OWM_TOKEN=your_token_open_wether_maps

set API_TOKEN=your_token_telegram_bot

python aiogram_main.py

pause