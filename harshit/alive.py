# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group
# Without Credit (Mother Fucker)
# Rocks © @Dr_Asad_Ali © Rocks
# Copyright (C) 2021 By @Itz_VeNom_xD 
# Copyright (C) 2021 By @Dr_Asad_Ali
# Copyright (C) 2021 By @HarshitSharma361

import asyncio
from time import time
from datetime import datetime
from rocks.helpers.filters import command
from rocks.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/a6205dbd405a78259ba5d.jpg",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
❤️ 𝐇𝐞𝐥𝐥𝐨, 𝐈 𝐚𝐦 𝐓𝐬𝐠 𝐌𝐮𝐬𝐢𝐜 𝐛𝐨𝐭 𝐟𝐮𝐥𝐥𝐲 𝐚𝐧𝐭𝐢𝐥𝐚𝐠 𝐚𝐧𝐝 𝐬𝐮𝐩𝐞𝐫𝐟𝐚𝐬𝐭 𝐦𝐮𝐬𝐢𝐜 𝐛𝐨𝐭
𝐅𝐨𝐫 𝐭𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐠𝐫𝐨𝐮𝐩𝐬❤️💝 ...
┏━━━━━━━━━━━━━━━━━┓
┣★ ᴄʀᴇᴀᴛᴏʀ : [Aman](https://t.me/itzamanrajput)
┣★ ᴜᴘᴅᴀᴛᴇs : [Channel](https://t.me/itsamanrajput)
┣★ sᴜᴘᴘᴏʀᴛ : [Tsg Chat](https://t.me/Friends_Chatting_Group3)
┣★ ᴏᴡɴᴇʀ › : [Tsg group owner](https://t.me/An_innocent_boy)
┗━━━━━━━━━━━━━━━━━┛

💞 ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ǫᴜᴇsᴛɪᴏɴs ᴛʜᴇɴ
ᴅᴍ ᴛᴏ ᴍʏ [𝐌𝐮𝐬𝐢𝐜 𝐛𝐨𝐭 𝐨𝐰𝐧𝐞𝐫](https://t.me/Itzamanrajput) ...
━━━━━━━━━━━━━━━━━━━━━━━━**""",
   reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ 𝐀𝐝𝐝 𝐓𝐬𝐠 𝐦𝐮𝐬𝐢𝐜 𝐛𝐨𝐭 𝐓𝐨 𝐲𝐨𝐮𝐫 𝐠𝐫𝐨𝐮𝐩 ❱ ➕", url=f"https://t.me/Music_tsgbot?startgroup=true")
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "/alive", "Tsg"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/a6205dbd405a78259ba5d.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "❤️ 𝐉𝐨𝐢𝐧 𝐡𝐞𝐫𝐞 𝐬𝐮𝐩𝐩𝐨𝐫𝐭 𝐠𝐫𝐨𝐮𝐩 💞", url=f"https://t.me/Friends_Chatting_Group3")
                ]
            ]
        ),
    )


@Client.on_message(commandpro(["repo", "#repo", "@repo", "/repo", "source"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/9ba3f9f51ac8958f1b61f.mp4",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🥀 𝒄𝒍𝒊𝒄𝒌 𝒎𝒆 𝒕𝒐 𝑮𝒆𝒕 𝒓𝒆𝒑𝒐 💞", url=f"https://t.me/itzamanrajput")
                ]
            ]
        ),
    )
