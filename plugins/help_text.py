import os

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config


from pyrogram import Client, filters
from translation import Translation


from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

START_TEXT = """Hҽʅʅ {}! I αɱ α Pσɯҽϝυʅ Hσƚʂƚαɾ URL Uρʅσαԃҽɾ Bσƚ 😎!"""

HELP_TEXT = """</b>SENT ANY LINK.......</b>\nTHAT'S ALL........\n\n</b>MADE BY </b>@TELSABOTS
"""

ABOUT_TEXT = """🤖</b>BOT🤖 : TELSA MEDIA INFO BOT</b>\n📢</b>CHANNEL📢 :</b> ❤️ <a href='https://t.me/telsabots'>TELSA BOTS</a>\n🧑🏼‍💻DEV🧑🏼‍💻: @ALLUADDICT\n__🤩SOURCE🤩:__ [👉CLICK HERE👈](https://t.me/SOURCE_TELSA/7)
"""
START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('📢CHANNEL📢', url='https://telegram.me/TELSABOTS'),
        InlineKeyboardButton('🧑🏼‍💻DEV🧑🏼‍💻', url='https://telegram.me/alluaddict')
        ],[
        InlineKeyboardButton('🤩YOUTUBE🤩', url='http://www.youtube.com/watch?v=nfWjbuQqgJc')
        ]]
    )

HELP_BUTTONS = InlineKeyboardMarkup(
       [[
        InlineKeyboardButton('📢CHANNEL📢', url='https://telegram.me/TELSABOTS'),
        InlineKeyboardButton('🧑🏼‍💻DEV🧑🏼‍💻', url='https://telegram.me/alluaddict')
        ],[
        InlineKeyboardButton('🤩YOUTUBE🤩', url='http://www.youtube.com/watch?v=nfWjbuQqgJc')
        ]]
    )
ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('📢CHANNEL📢', url='https://telegram.me/TELSABOTS'),
        InlineKeyboardButton('🧑🏼‍💻DEV🧑🏼‍💻', url='https://telegram.me/alluaddict')
        ],[
        InlineKeyboardButton('🤩YOUTUBE🤩', url='http://www.youtube.com/watch?v=nfWjbuQqgJc')
        ]]
    )
        
   
@Client.on_message(filters.command(["help"]))
async def help_message(bot, update):
    text=HELP_TEXT,,
    reply_markup = HELP_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )     

    
@Client.on_message(filters.command(["start"]))
async def start(bot, update):
    text=START_TEXT,
    reply_markup = START_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )
    
@Client.on_message(filters.command(["about"]))
async def about_message(bot, update):
    text=ABOUT_TEXT,
    reply_markup = ABOUT_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )     
    
