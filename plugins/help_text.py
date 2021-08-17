import os

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

from translation import Translation

from pyrogram import Client, filters

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton



START_TEXT = """HI I AM  TELSA URL UPLOADER BOT,
MADE BY @TELSABOTS
"""
HELP_USER = """It's not that complicated to use meh! 😅
    
1. Send Me A Tumbnail if required. It'll be saved permanently.💯
2. If Thumbnail Wasn't Set By You, It'll Be Auto Generated From The File.🥳
3. Send Me Any Link To Be Uploaded To Telegram.
4. Press /deletthumbnail To Delete Your Current Custom Thumbnail
5. Select the button.
   SVideo - Give File as video with Screenshots
   DFile  - Give File with Screenshots
   Video  - Give File as video without Screenshots
   DFile  - Give File without Screenshots
NB : It is Recommended To Use A Custom Thumbnail Because, Some Time Won't Upload The File Without a Custom Thumbnail.
Support Group : @TeleRoid14
"""

ABOUT_TEXT = """<b>🤖 BOT🤖 : TELSA URL UPLOADER BOT</b>
<b>🧑🏼‍💻DEV 🧑🏼‍💻 : 👉 <a href='https://t.me/ALLUADDICT'> ꧁༒☬𝓗𝓑☬༒꧂ </a></b>
<b> 📢CHANNEL📢 : 👉 <a href='https://t.me/TELSABOTS'> TELSA BOTS </a></b>"""
START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('📢CHANNEL📢', url='https://telegram.me/TELSABOTS'),
        InlineKeyboardButton('🧑🏼‍💻DEV🧑🏼‍💻', url='https://telegram.me/alluaddict')
        ],[
        InlineKeyboardButton('🆘HELP🆘', callback_data='help'),
        InlineKeyboardButton('🤗ABOUT🤗', callback_data='about'),
        InlineKeyboardButton('🔐CLOSE🔐', callback_data='close')
        ]]
    )

HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('📢CHANNEL📢', url='https://telegram.me/TELSABOTS'),
        InlineKeyboardButton('🧑🏼‍💻DEV🧑🏼‍💻', url='https://telegram.me/alluaddict')
        ],[
        InlineKeyboardButton('🏡HOME🏡', callback_data='home'),
        InlineKeyboardButton('🤗ABOUT🤗', callback_data='about'),
        InlineKeyboardButton('🔐CLOSE🔐', callback_data='close')
        ]]
    )
  
ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('📢CHANNEL📢', url='https://telegram.me/TELSABOTS'),
        InlineKeyboardButton('🧑🏼‍💻DEV🧑🏼‍💻', url='https://telegram.me/alluaddict')
        ],[
        InlineKeyboardButton('🏡HOME🏡', callback_data='home'),
        InlineKeyboardButton('🆘HELP🆘', callback_data='help'), 
        InlineKeyboardButton('🔐CLOSE🔐', callback_data='close')
        ]]
    )
@Client.on_callback_query()
async def cb_data(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text = START_TEXT,
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
        )
    elif update.data == "help":
        await update.message.edit_text(
            text = HELP_USER,
            disable_web_page_preview=True,
            reply_markup=HELP_BUTTONS
        )
    elif update.data == "about":
        await update.message.edit_text(
            text = ABOUT_TEXT,
            disable_web_page_preview=True,
            reply_markup=ABOUT_BUTTONS
        )
    else:
        await update.message.delete()
        
   
    
@Client.on_message(filters.command(["help"]))
async def help_message(bot, update):
    text = HELP_USER,
    reply_markup = HELP_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )     

    
@Client.on_message(filters.command(["start"]))
async def start(bot, update):
    text = START_TEXT,
    reply_markup = START_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )
    
@Client.on_message(filters.command(["about"]))
async def about_message(bot, update):
    text = ABOUT_TEXT,
    reply_markup = ABOUT_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )     
    
