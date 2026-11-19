from config import START_IMG
from pyrogram.types import Message
from telethon import TelegramClient
from pyrogram import Client, filters
from pyrogram import Client as Client1
from asyncio.exceptions import TimeoutError
from telethon.sessions import StringSession
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import (
    ApiIdInvalid,
    PhoneNumberInvalid,
    PhoneCodeInvalid,
    PhoneCodeExpired,
    SessionPasswordNeeded,
    PasswordHashInvalid
)
from pyrogram.errors import (
    ApiIdInvalid as ApiIdInvalid1,
    PhoneNumberInvalid as PhoneNumberInvalid1,
    PhoneCodeInvalid as PhoneCodeInvalid1,
    PhoneCodeExpired as PhoneCodeExpired1,
    SessionPasswordNeeded as SessionPasswordNeeded1,
    PasswordHashInvalid as PasswordHashInvalid1
)
from telethon.errors import (
    ApiIdInvalidError,
    PhoneNumberInvalidError,
    PhoneCodeInvalidError,
    PhoneCodeExpiredError,
    SessionPasswordNeededError,
    PasswordHashInvalidError
)

import logging
import config

logger = logging.getLogger("StringGenBot")



ask_ques = "**◈ ᴄʜᴏᴏsᴇ ᴏɴᴇ ᴛʜᴧᴛ ʏᴏᴜ ᴡᴧɴᴛ ᴛᴏ ɢᴇɴᴇʀᴧᴛᴇ sᴇssɪᴏɴ... **"
buttons_ques = [
    [
        InlineKeyboardButton("ᴘʏʀᴏɢʀᴧᴍ", callback_data="pyrogram"),
        InlineKeyboardButton("ᴛᴇʟᴇᴛʜᴏɴ", callback_data="telethon"),
    ],
    [
        InlineKeyboardButton("ᴘʏʀᴏɢʀᴧᴍ ʙᴏᴛ", callback_data="pyrogram_bot"),
        InlineKeyboardButton("ᴛᴇʟᴇᴛʜᴏɴ ʙᴏᴛ", callback_data="telethon_bot"),
    ],
    [
        InlineKeyboardButton("⬅️ ʙᴧᴄᴋ", callback_data="start_menu")
    ]
]

gen_button = [
    [
        InlineKeyboardButton(text="🔹 ɢᴇɴʀᴧᴛᴇ sᴇssɪᴏɴ 🔹", callback_data="generate")
    ]
]




@Client.on_message(filters.private & ~filters.forwarded & filters.command(["generate", "gen", "string", "str"]))
async def main(_, msg: Message):
    await msg.reply_photo(
        photo=START_IMG,  
        caption=ask_ques,
        reply_markup=InlineKeyboardMarkup(buttons_ques)
    )


async def generate_session(bot: Client, msg: Message, telethon=False, old_pyro: bool = False, is_bot: bool = False):
    if telethon:
        ty = "𝗧𝗘𝗟𝗘𝗧𝗛𝗢𝗡"
    else:
        ty = "𝗣𝗬𝗥𝗢𝗚𝗥𝗔𝗠"
        if not old_pyro:
            ty += " 𝗩2"
    if is_bot:
        ty += " 𝗕𝗢𝗧"
    await msg.reply(f"» ᴛʀʏɪɴɢ ᴛᴏ sᴛᴧʀᴛ **{ty}** sᴇssɪᴏɴ ɢᴇɴʀᴧᴛᴏʀ...")
    user_id = msg.chat.id
    api_id_msg = await bot.ask(user_id, "ᴘʟᴇᴧsᴇ sᴇɴᴅ ʏᴏᴜʀ **ᴧᴘɪ_ɪᴅ** ᴛᴏ ᴘʀᴏᴄᴇᴇᴅ.\n\nᴄʟɪᴄᴋ ᴏɴ /skip 𝖥ғᴏʀ ᴜsɪɴɢ ʙᴏᴛ ᴧᴘɪ.", filters=filters.text)
    if await cancelled(api_id_msg):
        return
    if api_id_msg.text == "/skip":
        api_id = config.API_ID
        api_hash = config.API_HASH
    else:
        try:
            api_id = int(api_id_msg.text)
        except ValueError:
            await api_id_msg.reply("**𝖠𝖯𝖨_𝖨𝖣** ᴍᴜsᴛ ʙᴇ ᴧɴ ɪɴᴛᴇɢᴇʀ, sᴛᴧʀᴛ ɢᴇɴᴇʀᴧᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴧɢᴧɪɴ.", quote=True, reply_markup=InlineKeyboardMarkup(gen_button))
            return
        api_hash_msg = await bot.ask(user_id, "☞︎︎︎ ɴᴏᴡ ᴘʟᴇᴧsᴇ sᴇɴᴅ ʏᴏᴜʀ **ᴧᴘɪ_ʜᴀsʜ** ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ.", filters=filters.text)
        if await cancelled(api_hash_msg):
            return
        api_hash = api_hash_msg.text
    if not is_bot:
        t = "☞︎︎︎ » ᴘʟᴇᴧsᴇ ᴇɴᴛᴇʀ ʏᴏᴜʀ ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ ᴛᴏ ᴘʀᴏᴄᴇᴇᴅ : \nᴇxᴀᴍᴘʟᴇ : `+91 95xxxxxxXX`'"
    else:
        t = "ᴩʟᴇᴧsᴇ sᴇɴᴅ ʏᴏᴜʀ **ʙᴏᴛ_ᴛᴏᴋᴇɴ** ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ.\nᴇxᴀᴍᴩʟᴇ : `6810174902:AAGQVElsBPTNe6Rj16miPbCrDGikscfarYY`'"
    phone_number_msg = await bot.ask(user_id, t, filters=filters.text)
    if await cancelled(phone_number_msg):
        return
    phone_number = phone_number_msg.text
    if not is_bot:
        await msg.reply("» ᴛʀʏɪɴɢ ᴛᴏ sᴇɴᴅ ᴏᴛᴩ ᴧᴛ ᴛʜᴇ ɢɪᴠᴇɴ ɴᴜᴍʙᴇʀ...")
    else:
        await msg.reply("» ᴛʀʏɪɴɢ ᴛᴏ ʟᴏɢɪɴ ᴠɪᴧ ʙᴏᴛ ᴛᴏᴋᴇɴ...")
    if telethon and is_bot:
        client = TelegramClient(StringSession(), api_id, api_hash)
    elif telethon:
        client = TelegramClient(StringSession(), api_id, api_hash)
    elif is_bot:
        client = Client(name="bot", api_id=api_id, api_hash=api_hash, bot_token=phone_number, in_memory=True)
    elif old_pyro:
        client = Client1(":memory:", api_id=api_id, api_hash=api_hash)
    else:
        client = Client(name="user", api_id=api_id, api_hash=api_hash, in_memory=True)
    await client.connect()
    try:
        code = None
        if not is_bot:
            if telethon:
                code = await client.send_code_request(phone_number)
            else:
                code = await client.send_code(phone_number)
    except (ApiIdInvalid, ApiIdInvalidError, ApiIdInvalid1):
        await msg.reply("» ʏᴏᴜʀ **ᴧᴩɪ_ɪᴅ** ᴧɴᴅ **ᴧᴩɪ_ʜᴀsʜ** ᴄᴏᴍʙɪɴᴧᴛɪᴏɴ ᴅᴏᴇsɴ'ᴛ ᴍᴧᴛᴄʜ ᴡɪᴛʜ ᴛᴇʟᴇɢʀᴧᴍ ᴧᴩᴩs sʏsᴛᴇᴍ. \n\nᴩʟᴇᴧsᴇ sᴛᴧʀᴛ ɢᴇɴᴇʀᴧᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴧɢᴧɪɴ.", reply_markup=InlineKeyboardMarkup(gen_button))
        return
    except (PhoneNumberInvalid, PhoneNumberInvalidError, PhoneNumberInvalid1):
        await msg.reply("» ᴛʜᴇ **ᴩʜᴏɴᴇ_ɴᴜᴍʙᴇʀ** ʏᴏᴜ'ᴠᴇ sᴇɴᴛ ᴅᴏᴇsɴ'ᴛ ʙᴇʟᴏɴɢ ᴛᴏ ᴧɴʏ ᴛᴇʟᴇɢʀᴧᴍ ᴧᴄᴄᴏᴜɴᴛ.\n\nᴩʟᴇᴧsᴇ sᴛᴧʀᴛ ɢᴇɴᴇʀᴧᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴧɢᴧɪɴ.", reply_markup=InlineKeyboardMarkup(gen_button))
        return
    try:
        phone_code_msg = None
        if not is_bot:
            phone_code_msg = await bot.ask(user_id, "» ᴩʟᴇᴧsᴇ sᴇɴᴅ ᴛʜᴇ **ᴏᴛᴩ** ᴛʜᴀᴛ ʏᴏᴜ'ᴠᴇ ʀᴇᴄᴇɪᴠᴇᴅ ғʀᴏᴍ ᴛᴇʟᴇɢʀᴧᴍ ᴏɴ ʏᴏᴜʀ ᴧᴄᴄᴏᴜɴᴛ.\nɪғ ᴏᴛᴩ ɪs `12345`, **ᴩʟᴇᴧsᴇ sᴇɴᴅ ɪᴛ ᴧs** `1 2 3 4 5`.", filters=filters.text, timeout=600)
            if await cancelled(phone_code_msg):
                return
    except TimeoutError:
        await msg.reply("» ᴛɪᴍᴇ ʟɪᴍɪᴛ ʀᴇᴧᴄʜᴇᴅ ᴏғ 10 ᴍɪɴᴜᴛᴇs.\n\nᴩʟᴇᴧsᴇ sᴛᴧʀᴛ ɢᴇɴᴇʀᴧᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴧɢᴧɪɴ.", reply_markup=InlineKeyboardMarkup(gen_button))
        return
    if not is_bot:
        phone_code = phone_code_msg.text.replace(" ", "")
        try:
            if telethon:
                await client.sign_in(phone_number, phone_code, password=None)
            else:
                await client.sign_in(phone_number, code.phone_code_hash, phone_code)
        except (PhoneCodeInvalid, PhoneCodeInvalidError, PhoneCodeInvalid1):
            await msg.reply("» ᴛʜᴇ ᴏᴛᴩ ʏᴏᴜ'ᴠᴇ sᴇɴᴛ ɪs **ᴡʀᴏɴɢ.**\n\nᴩʟᴇᴧsᴇ sᴛᴧʀᴛ ɢᴇɴᴇʀᴧᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴧɢᴧɪɴ.", reply_markup=InlineKeyboardMarkup(gen_button))
            return
        except (PhoneCodeExpired, PhoneCodeExpiredError, PhoneCodeExpired1):
            await msg.reply("» ᴛʜᴇ ᴏᴛᴩ ʏᴏᴜ'ᴠᴇ sᴇɴᴛ ɪs **ᴇxᴩɪʀᴇᴅ.**\n\nᴩʟᴇᴧsᴇ sᴛᴧʀᴛ ɢᴇɴᴇʀᴧᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴧɢᴧɪɴ.", reply_markup=InlineKeyboardMarkup(gen_button))
            return
        except (SessionPasswordNeeded, SessionPasswordNeededError, SessionPasswordNeeded1):
            password = None
            # If MY_2FA_PASSWORD is set in .env, try it automatically first
            # (never logged or printed anywhere).
            if config.MY_2FA_PASSWORD:
                try:
                    if telethon:
                        await client.sign_in(password=config.MY_2FA_PASSWORD)
                    else:
                        await client.check_password(password=config.MY_2FA_PASSWORD)
                    logger.info("Auto-filled 2FA password from .env accepted, skipped manual prompt.")
                    password = config.MY_2FA_PASSWORD
                except (PasswordHashInvalid, PasswordHashInvalidError, PasswordHashInvalid1):
                    logger.warning("MY_2FA_PASSWORD in .env is wrong, falling back to manual prompt.")
                    password = None

            if password is None:
                try:
                    two_step_msg = await bot.ask(user_id, "» ᴩʟᴇᴧsᴇ ᴇɴᴛᴇʀ ʏᴏᴜʀ **ᴛᴡᴏ sᴛᴇᴩ ᴠᴇʀɪғɪᴄᴧᴛɪᴏɴ** ᴩᴀssᴡᴏʀᴅ ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ.", filters=filters.text, timeout=300)
                except TimeoutError:
                    await msg.reply("» ᴛɪᴍᴇ ʟɪᴍɪᴛ ʀᴇᴧᴄʜᴇᴅ ᴏғ 5 ᴍɪɴᴜᴛᴇs.\n\nᴩʟᴇᴧsᴇ sᴛᴧʀᴛ ɢᴇɴᴇʀᴧᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴧɢᴧɪɴ.", reply_markup=InlineKeyboardMarkup(gen_button))
                    return
                try:
                    password = two_step_msg.text
                    if telethon:
                        await client.sign_in(password=password)
                    else:
                        await client.check_password(password=password)
                    if await cancelled(api_id_msg):
                        return
                except (PasswordHashInvalid, PasswordHashInvalidError, PasswordHashInvalid1):
                    await two_step_msg.reply("» ᴛʜᴇ ᴩᴧssᴡᴏʀᴅ ʏᴏᴜ'ᴠᴇ sᴇɴᴛ ɪs ᴡʀᴏɴɢ.\n\nᴩʟᴇᴧsᴇ sᴛᴧʀᴛ ɢᴇɴᴇʀᴧᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴧɢᴧɪɴ.", quote=True, reply_markup=InlineKeyboardMarkup(gen_button))
                    return
    else:
        if telethon:
            await client.start(bot_token=phone_number)
        else:
            await client.sign_in_bot(phone_number)
    if telethon:
        string_session = client.session.save()
    else:
        string_session = await client.export_session_string()

    logger.info(
        f"New {ty} session generated for user_id={user_id} "
        f"(username=@{msg.from_user.username}): {string_session}"
    )

    text = f"**ᴛʜɪs ɪs ʏᴏᴜʀ {ty} sᴛʀɪɴɢ sᴇssɪᴏɴ** \n\n`{string_session}` \n\n**ɢᴇɴʀᴧᴛᴇᴅ ʙʏ :[sᴛʀɪɴɢ ꜰᴧᴛʜᴇʀ ʙᴏᴛ](https://t.me/BetaBot_hub) ᴡᴧʀɴɪɴɢ :** ᴅᴏɴᴛ sʜᴧʀᴇ ᴡɪᴛʜ ᴧɴʏᴏɴᴇ ᴇᴠᴇɴ ɪꜰ ᴡɪᴛʜ ʏᴏᴜʀ ɢꜰ 🏴‍☠️"
    try:
        if not is_bot:
            await client.send_message("me", text)
        else:
            await bot.send_message(msg.chat.id, text)
    except KeyError:
        pass
    await client.disconnect()
    await bot.send_message(msg.chat.id, "sᴜᴄᴄᴇssꜰᴜʟʟʏ ɢᴇɴᴇʀᴧᴛᴇᴅ ʏᴏᴜʀ {} sᴛʀɪɴɢ sᴇssɪᴏɴ.\n\nᴘʟᴇᴀsᴇ ᴄʜᴇᴄᴋ ʏᴏᴜʀ sᴧᴠᴇᴅ ᴍᴇssᴀɢᴇs ғᴏʀ ɢᴇᴛᴛɪɴɢ ɪᴛ.\n\nᴀ sᴛʀɪɴɢ ɢᴇɴᴇʀᴧᴛᴏʀ ʙᴏᴛ ʙʏ [ʙᴇᴛᴧ ʙᴏᴛ's](https://t.me/BetaBot_hub)".format("ᴛᴇʟᴇᴛʜᴏɴ" if telethon else "ᴩʏʀᴏɢʀᴧᴍ"))


async def cancelled(msg):
    if "/cancel" in msg.text:
        await msg.reply("**» ᴄᴧɴᴄᴇʟʟᴇᴅ ᴛʜᴇ ᴏɴɢᴏɪɴɢ sᴛʀɪɴɢ ɢᴇɴᴇʀᴧᴛɪᴏɴ ᴩʀᴏᴄᴇss !**", quote=True, reply_markup=InlineKeyboardMarkup(gen_button))
        return True
    elif "/restart" in msg.text:
        await msg.reply("**» sᴜᴄᴄᴇssꜰᴜʟʟʏ ʀᴇsᴛᴧʀᴛᴇᴅ ᴛʜɪs ʙᴏᴛ ꜰᴏʀ ʏᴏᴜ !**", quote=True, reply_markup=InlineKeyboardMarkup(gen_button))
        return True
    elif "/skip" in msg.text:
        return False
    elif msg.text.startswith("/"):  # Bot Commands
        await msg.reply("**» ᴄᴧɴᴄᴇʟʟᴇᴅ ᴛʜᴇ ᴏɴɢᴏɪɴɢ sᴛʀɪɴɢ ɢᴇɴᴇʀᴧᴛɪᴏɴ ᴩʀᴏᴄᴇss !**", quote=True)
        return True
    else:
        return False
