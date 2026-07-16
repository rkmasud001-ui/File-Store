import os
from os import environ, getenv
import logging
from dotenv import load_dotenv

load_dotenv()
from logging.handlers import RotatingFileHandler

#--------------------------------------------
#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
APP_ID = int(os.environ.get("APP_ID", "30800287"))
API_HASH = os.environ.get("API_HASH", "6d4de3e85c8b20beccb92439c57aa398")
#--------------------------------------------

CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "0"))
OWNER = os.environ.get("OWNER", "")
OWNER_ID = int(os.environ.get("OWNER_ID", "8075531485"))
#--------------------------------------------
PORT = os.environ.get("PORT", "8001")
#--------------------------------------------
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://otakumongo8:otakumongo8@cluster0.kiy5lxh.mongodb.net/?appName=Cluster0")

if not TG_BOT_TOKEN:
    logging.warning("TG_BOT_TOKEN is not set!")
if APP_ID == 0:
    logging.warning("APP_ID is not set!")
if not API_HASH:
    logging.warning("API_HASH is not set!")
if not DB_URI:
    logging.warning("DATABASE_URL is not set!")
DB_NAME = os.environ.get("Filestore", "")
#--------------------------------------------
FSUB_LINK_EXPIRY = int(os.getenv("FSUB_LINK_EXPIRY", "10"))  # 0 means no expiry
BAN_SUPPORT = os.environ.get("BAN_SUPPORT", "https://t.me/ZoroAnimeSupport")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "200"))
#--------------------------------------------
START_PIC = os.environ.get("START_PIC", "https://graph.org/file/0591ce5558c3ec8fe7612-263292508134daf3e1.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://graph.org/file/fdc4357abfaba23255e98-24d1bbfa3888cdfcfe.jpg")
#--------------------------------------------

#--------------------------------------------
HELP_TXT = "<b><blockquote>⚡ This is a <u>Private Premium Bot</u> – Only admins & management can operate it.\n🔐 To get the bot link and access its features, join our mentioned channel and click the direct link provided.\n🎯 This bot is exclusively for <b>VIP & special users</b>, giving you instant file access securely and privately!</blockquote></b>\n\n<b>•Join Our Main Channel: @Zoro_Anime_Zone\nFore More Information Use /help</b>"

# Isko clean kar diya hai taaki line breaks sahi se aayein
ABOUT_TXT = """<b>🤖 Kaoruko Waguri Bot - About</b>

<b><blockquote>💡 Bot Status: <code>Online 24/7</code>
🚀 Features: Instant Anime & File Access, Special Channel Links.
🔗 Access: Get files directly via special links.
⚡ Uptime: Always active for your convenience.
🌐 Channels: Join to explore more anime content.</blockquote></b>
<b><blockquote>◈ ᴄʀᴇᴀᴛᴏʀ: <a href="https://t.me/Animezone236">Nippi</a>\n◈ ꜰᴏᴜɴᴅᴇʀ ᴏꜰ: <a href="https://t.me/Zoro_Anime_Zone">Zoro Anime Zone</a>\n◈ ᴅᴇᴠᴇʟᴏᴘᴇʀ: <a href="https://t.me/UNRATED_CODER">UNRATED CODER</a></blockquote></b>"""
#--------------------------------------------
#--------------------------------------------
START_MSG = os.environ.get("START_MESSAGE", "<b>💖 Hᴇʟʟᴏ {first}!🥀\n\n<blockquote>I ᴀᴍ Kaoruko Waguri ✨ Your Personal Anime & File Access Bot🚀 I ᴄᴀɴ sᴀᴠᴇ ᴘʀɪᴠᴀᴛᴇ ғɪʟᴇs ɪɴ ᴄʜᴀɴɴᴇʟs🔗 & Gɪᴠᴇ ʏᴏᴜ ᴀᴄᴄᴇss via a Special Link</blockquote>\n<blockquote>🔰 Check Out Our Channels & Get Files Instantly! 🔰</blockquote></b>")
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b>🚨 Please Join Our Channels First!</b>\n\n<blockquote>⚡ To continue using this bot, make sure you've joined all the required channels mentioned below.\nOnce done, click the <b>TRY AGAIN</b> button to verify your access!</blockquote>\n\n<blockquote>💡 If you're facing any issue using the bot, type <code>/help</code> to watch the full tutorial and fix it easily!</blockquote>")

CMD_TXT = """<blockquote><b>» ᴀᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴅs:</b></blockquote>

<b>›› /dlt_time :</b> sᴇᴛ ᴀᴜᴛᴏ ᴅᴇʟᴇᴛе ᴛɪᴍᴇ
<b>›› /check_dlt_time :</b> ᴄʜᴇᴄᴋ ᴄᴜʀʀᴇɴᴛ ᴅᴇʟᴇᴛе ᴛɪᴍᴇ
<b>›› /dbroadcast :</b> ʙʀᴏᴀᴅᴄᴀsᴛ ᴅᴏᴄᴜᴍᴇɴᴛ / ᴠɪᴅᴇᴏ
<b>›› /ban :</b> ʙᴀɴ ᴀ ᴜꜱᴇʀ
<b>›› /unban :</b> ᴜɴʙᴀɴ ᴀ ᴜꜱᴇʀ
<b>›› /banlist :</b> ɢᴇᴛ ʟɪsᴛ ᴏꜰ ʙᴀɴɴᴇᴅ ᴜꜱᴇʀs
<b>›› /addchnl :</b> ᴀᴅᴅ ꜰᴏʀᴄᴇ sᴜʙ ᴄʜᴀɴɴᴇʟ
<b>›› /delchnl :</b> ʀᴇᴍᴏᴠᴇ ꜰᴏʀᴄᴇ sᴜʙ ᴄʜᴀɴɴᴇʟ
<b>›› /listchnl :</b> ᴠɪᴇᴡ ᴀᴅᴅᴇᴅ ᴄʜᴀɴɴᴇʟs
<b>›› /fsub_mode :</b> ᴛᴏɢɢʟᴇ ꜰᴏʀᴄᴇ sᴜʙ ᴍᴏᴅᴇ
<b>›› /pbroadcast :</b> sᴇɴᴅ ᴘʜᴏᴛᴏ ᴛᴏ ᴀʟʟ ᴜꜱᴇʀs
<b>›› /add_admin :</b> ᴀᴅᴅ ᴀɴ ᴀᴅᴍɪɴ
<b>›› /deladmin :</b> ʀᴇᴍᴏᴠᴇ ᴀɴ ᴀᴅᴍɪɴ
<b>›› /admins :</b> ɢᴇᴛ ʟɪsᴛ ᴏꜰ ᴀᴅᴍɪɴs
"""
#--------------------------------------------
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>• ʙʏ @Zoro_Anime_Zone</b>") 
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False 
#--------------------------------------------
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'
#--------------------------------------------
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "<b>ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!</b>"
USER_ROAST_TEXT = "<b>ᴡʜᴏ ᴀʀᴇ ʏᴏᴜ ᴛᴏ ʙᴀɴ ᴀɴʏᴏɴᴇ? Kɴᴏᴡ ʏᴏᴜʀ ᴘʟᴀᴄᴇ ғɪʀsᴛ.</b>"
#--------------------------------------------

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
