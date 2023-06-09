import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/anunicn47/Telegram")

class Config(object):
    log = True
    APP_ID = getenv("API_ID", "14005742")
    API_HASH = getenv("API_HASH", "14b504e0fde7bdaa720d907270dddcaf")
    TOKEN = getenv("TOKEN", "")
    OWNER_ID = getenv("OWNER_ID", "")
    ASSISTANT_ID = getenv("ASSISTANT_ID", "")
    STRING_SESSION = getenv("STRING_SESSION", "") #telethon
    OWNER_USERNAME = getenv("OWNER_USERNAME", "")
    DB_URI = getenv("DATABASE_URL", "")
    DB_URI = DB_URI.replace("postgres", "postgresql")
    MESSAGE_DUMP = getenv("MESSAGE_DUMP", "-1001509712478")
    GBAN_LOGS = getenv("GBAN_LOGS", "-1001509712478")
    SYS_ADMIN = getenv("SYS_ADMIN", "6032807619")
    DEV_USERS = getenv("DEV_USERS", "6032807619")
    LOAD = getenv("LOAD")
    WEBHOOK = False
    SPB_MODE = True
    DROP_UPDATES = False
    DEBUG = False
    URL = None
    INFOPIC = True
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True
    STRICT_GBAN = True
    BAN_STICKER = getenv("BAN_STICKER", "")
    ALLOW_EXCL = True
    CUSTOM_CMD = False
    CHANNEL = getenv("CHANNEL", "puiisupportchat")
    SUPPORT = getenv("SUPPORT", "puiisupportchat")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    CASH_API_KEY = getenv("CASH_API_KEY", "https://www.alphavantage.co/support/#api-key")
    TIME_API_KEY = getenv("TIME_API_KEY", "https://timezonedb.com/api")
    WALL_API = getenv("WALL_API", "https://wall.alphacoders.com/api.php")
    spamwatch_api = getenv("spamwatch_api", "https://t.me/SpamWatchBot")
    SPAMMERS = getenv("SPAMMERS", "")
    LASTFM_API_KEY = getenv("LASTFM_API_KEY", "https://www.last.fm/api/account/create")
    CF_API_KEY = getenv("CF_API_KEY", "coffehouse.intellivoid.net")
    BOT_API_URL = getenv("BOT_API_URL", "https://api.telegram.org/bot")
    BOT_API_FILE_URL = getenv("BOT_API_FILE_URL", "https://api.telegram.org/file/bot")
    SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6032807619").split()))
    ZAID_USER = list(map(int, getenv("DEV_USERS", "6032807619").split()))
    NO_LOAD = list(map(int, getenv("NO_LOAD", "").split()))
