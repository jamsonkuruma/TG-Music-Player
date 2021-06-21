from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def karwan(_, message: Message):
    await message.reply_text(
        f"""I am an nezoku 👇this is my developers👇

join my developer gruops and shapport me :- @SL_MEDIA_TECH_GRUOP , @NovaTechlk
My developers

🌟AKILA :-  @Akilawiduruwan
🌟PAHAN :- @Humangasor
my music play command 👇
/mute - 🔇 Mute the user bot
/stop - 🔊 clear play list
/play :- play a song
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Group", url="https://t.me/SL_MEDIA_TECH_GRUOP"
                    ),
                    InlineKeyboardButton(
                        "Channel", url="https://t.me/sl_media_tech"
                    )
                ]
            ]
        )
    )
