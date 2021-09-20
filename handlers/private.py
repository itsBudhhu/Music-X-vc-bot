from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2

@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAAEC7uFhSDXAizy1JzcPt_rnp7gp0XOTtgACtwQAAmliQFbPe4RUL9O10CAE")
    await message.reply_text(
        f"""**Hey, I'm {bn} 🎵

I'm music of @SAIFALISEW1508 For group's voice call. Developed by [𓆩ꀤຖᎠꀤꋫຖ𓆪 [• 🇮🇳 •]ᏕᎯᎥʆ](https://t.me/SAIFALISEW1508).

If you want to Deploy Own Bot For Your group Contact @SAIFALISEW1508**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🥀DEVLOPER🥀", url="https://t.me/SAIFALISEW1508")
                  ],[ 
                    InlineKeyboardButton(
                        "😍SUPPORT CHAT😍", url="https://t.me/MYSTERIOUS_EMPIRE"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Music Player Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "CONTACT OWNER", url="https://t.me/SAIFALISEW1508")
                ]
            ]
        )
   )

