from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""Hᴇʏ {msg.from_user.mention},

Tʜɪs ɪs {me2},
 sᴛʀɪɴɢ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ, ᴡʀɪᴛᴛᴇɴ ɪɴ ᴩʏᴛʜᴏɴ ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴩ ᴏғ ᴩʏʀᴏɢʀᴀᴍ.

Mᴀᴅᴇ 💛 ʙʏ : [⌜NOBITA⌝](tg://user?id={OWNER_ID}) !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="🦋 ɢᴇɴᴇʀᴀᴛᴇ sᴇssɪᴏɴ 🦋", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("⌑ Channel ⌑", url="https://t.me/Want_To_Know_Mee"),
                    InlineKeyboardButton("⌑ ᴅᴇᴠᴇʟᴏᴩᴇʀ ⌑", user_id=OWNER_ID)
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
