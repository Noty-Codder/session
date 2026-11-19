from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")

OWNER_ID = int(getenv("OWNER_ID", ""))
# Optional: your own 2FA password, auto-filled during session generation
# so you don't have to type it (and it never gets logged or printed).
MY_2FA_PASSWORD = getenv("MY_2FA_PASSWORD", "")
# Telegram channel/group ID where the bot sends its logs (startup, session
# generated, errors). Bot must be a member/admin of this chat.
_raw_log_channel = getenv("LOG_CHANNEL", "0").strip().strip('"').strip("'")
try:
    LOG_CHANNEL = int(_raw_log_channel) if _raw_log_channel else 0
except ValueError:
    LOG_CHANNEL = 0
MONGO_DB_URI = getenv("MONGO_DB_URI", "")
MUST_JOIN = getenv("MUST_JOIN", "")
START_IMG = getenv("START_IMG", "")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "")
UPDATE_CHANNEL = getenv("UPDATE_CHANNEL", "")
