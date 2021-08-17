import os

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

from translation import Translation

from pyrogram import Client, filters

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton



START_TEXT = """HI {},
I AM @TELSA URL UPLOADER BOT

MADE BY @TELSABOTS
"""

HELP_TEXT = """
</b>SENT ANY LINK.......</b>

THAT'S ALL........

</b>MADE BY </b>@TELSABOTS
"""

ABOUT_TEXT = """
🤖</b>BOT🤖 : TELSA MEDIA INFO BOT</b>
 
📢</b>CHANNEL📢 :</b> ❤️ <a href='https://t.me/telsabots'>TELSA BOTS</a>
🧑🏼‍💻DEV🧑🏼‍💻: @ALLUADDICT
__🤩SOURCE🤩:__ [👉CLICK HERE👈](https://t.me/SOURCE_TELSA/7)
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
    text = HELP_TEXT,
    reply_markup = HELP_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )     

    
@Client.on_message(filters.command(["start"]))
async def start(bot, update):
    text = START_TEXT.format(update.from_user.mention),
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
    
