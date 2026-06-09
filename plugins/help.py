import asyncio
from pyrogram import Client, filters, enums
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from bot import Bot  # your bot instance
from pyrogram.enums import ParseMode


HELP_IMAGE_URL = "https://graph.org/file/927bf2751b931e2496aed-0dbc57797e8526bad4.jpg"

HELP_TEXT = """<b>🥰 Kon’nichiwa USER_MENTION_PLACEHOLDER! ~</b>\n\n
<blockquote><b>⚔️ I’ᴍ ᴀɴ ᴀɴɪᴍᴇ-ᴛʜᴇᴍᴇᴅ ғɪʟᴇ ʙᴏᴛ 🎥\n
Bᴏʀɴ ɪɴ ᴛʜᴇ ʀᴇᴀʟᴍ ᴏғ ᴅᴀᴛᴀ ᴀɴᴅ ᴄᴏᴅᴇ, I sᴇʀᴠᴇ ᴛᴏ ᴅᴇʟɪᴠᴇʀ sᴘᴇᴄɪᴀʟ ᴀɴɪᴍᴇ ғɪʟᴇs ᴛᴏ ᴛʜᴇ ᴡᴏʀᴛʜʏ ⚡\n\n
💮 Tᴏ ᴀᴄᴄᴇss ᴍʏ sᴇᴄʀᴇᴛ ᴀʀᴄʜɪᴠᴇs, ʏᴏᴜ ᴍᴜsᴛ ᴊᴏɪɴ ᴀʟʟ ᴛʜᴇ ᴀʟʟɪᴇᴅ ᴄʜᴀɴɴᴇʟs 🎯\n
Oɴʟʏ ᴛʜᴇ ᴘᴏʀᴛᴀʟ ᴡɪʟʟ ᴏᴘᴇɴ 🔓\n\n
🌌 Oɴᴄᴇ ʏᴏᴜ’ʀᴇ ɪɴ, ᴛʜᴇ ғɪʟᴇs ᴡɪʟʟ ʀᴇᴠᴇᴀʟ ᴛʜᴇɪʀ ᴛʀᴜᴛʜ 💫\n
Aɴɪᴍᴇ sᴘɪʀɪᴛs ᴀʀᴇ ᴡᴀɪᴛɪɴɢ ғᴏʀ ʏᴏᴜ 🌀</b></blockquote>\n\n

<b>🪄 How To Use The Bot?</b>\n\n
<blockquote>
<b>⚙️ Don’t know how to use this bot? No worries! 😄\n
Just follow our simple step-by-step tutorial to understand everything easily.</b>\n\n
👉 <b><a href="https://t.me/AniReal_Updates/107">Click Here To Watch The Tutorial 🎬</a></b>
</blockquote>

<b>» Users Commands:</b>\n
<blockquote>‣ <b>/start</b> - Start the bot! 🟢\n
‣ <b>/help</b> – Summon the help menu 📜</blockquote>\n\n

<b>» Admin Commands:</b>\n
<blockquote>
<b>›› /dlt_time :</b> Set auto delete time\n
<b>›› /check_dlt_time :</b> Check current delete time\n
<b>›› /dbroadcast :</b> Broadcast document / video\n
<b>›› /ban :</b> Ban a user\n
<b>›› /unban :</b> Unban a user\n
<b>›› /banlist :</b> Get list of banned users\n
<b>›› /addchnl :</b> Add force-sub channel\n
<b>›› /delchnl :</b> Remove force-sub channel\n
<b>›› /listchnl :</b> View added channels\n
<b>›› /fsub_mode :</b> Toggle force-sub mode\n
<b>›› /pbroadcast :</b> Send photo to all users\n
<b>›› /add_admin :</b> Add an admin\n
<b>›› /deladmin :</b> Remove an admin\n
<b>›› /admins :</b> Get list of admins</blockquote>\n\n

<b>◈ Need Assistance? Contact my Master through the button below ⚙️</b>"""
# =====================

@Bot.on_message(filters.command("help") & filters.private)
async def help_command(client: Client, message: Message):
    user_mention = f"<a href='tg://user?id={message.from_user.id}'>➣ {message.from_user.first_name}</a>"

    # Step 1: Loading animation
    loading = await message.reply_text("Loading!")
    for dots in ["!!", "!!!", "!!!!", "!!!!!"]:
        await asyncio.sleep(0.5)
        await client.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
        await loading.edit_text(f"Loading{dots}")

    await asyncio.sleep(0.5)
    await loading.delete()

    # Step 2: Send help message
    # Caption limit is 1024, HELP_TEXT is ~1500. So we send photo then text.
    await client.send_photo(
        chat_id=message.chat.id,
        photo=HELP_IMAGE_URL
    )

    await client.send_message(
        chat_id=message.chat.id,
        text=HELP_TEXT.replace("USER_MENTION_PLACEHOLDER", user_mention),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("• ᴏᴡɴᴇʀ", url="https://t.me/UNRATED_CODER"),
                    InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ •", url="https://t.me/UNRATED_CODER")
                ],
                [
                    InlineKeyboardButton("• Jᴏɪɴ ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ •", url="https://t.me/UNRATED_CODER")
                ],
            ]
        ),
        parse_mode=ParseMode.HTML
    )
