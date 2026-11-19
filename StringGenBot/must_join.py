import logging
from config import MUST_JOIN

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden

logger = logging.getLogger("StringGenBot")


@Client.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not MUST_JOIN:
        return
    try:
        try:
            await bot.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/" + MUST_JOIN
            else:
                chat_info = await bot.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                await msg.reply_photo(
                    photo="https://files.catbox.moe/j2v23d.jpg", caption=f"**» ꜰɪʀsᴛʟʏ ʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ ᴊᴏɪɴ ᴏᴜʀ ꜰᴧᴍɪʟʏ ᴛʜᴇɴ ʏᴏᴜ ᴄᴧɴ ᴜsᴇ ᴍᴇ.\n\n➥ ᴊᴏɪɴ [ᴜᴘᴅᴧᴛᴇs]({link}).\n\n» ᴧꜰᴛᴇʀ ᴊᴏɪɴ /start ᴍᴇ ᴧɢᴧɪɴ 🌹!**",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇs", url=link),
                            ]
                        ]
                    )
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        logger.error(f"Bot is NOT an admin in the MUST_JOIN chat ({MUST_JOIN}). Promote it to admin there.")
