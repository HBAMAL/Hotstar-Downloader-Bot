import os

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

from translation import Translation

from pyrogram import Client, filters

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

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
            text=START_TEXT.format(update.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=Translation.HELP_USER,
            disable_web_page_preview=True,
            reply_markup=HELP_BUTTONS
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=Translation.ABOUT_TEXT,
            disable_web_page_preview=True,
            reply_markup=ABOUT_BUTTONS
        )
    else:
        await update.message.delete()
        
   
    
@Client.on_message(filters.command(["help"]))
async def help_message(bot, update):
    text=Translation.HELP_USER,
    reply_markup = HELP_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )     


@Client.on_message(filters.command(["start"]))
async def start(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="⭕️ CHANNEL ⭕️", url="https://t.me/telsabots")], [InlineKeyboardButton(text="DEV", url="https://t.me/alluaddict"),
                                                    InlineKeyboardButton(text="About Meh👤", url="https://t.me/TheTeleRoid")]]),
    )

@Client.on_message(filters.command(["about"]))
async def about_message(bot, update):
    text=Translation.ABOUT_TEXT,
    reply_markup = ABOUT_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )     
    
