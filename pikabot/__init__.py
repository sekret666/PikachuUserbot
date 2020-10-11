import os ; import sys ; from pymongo import MongoClient ; from telethon.sessions import StringSession ; from telethon import TelegramClient ; from telethon.tl.types import PeerChannel ; from var import Var ; import time ; UpTime = time.time() ; from .sql_helper.global_variables import * ;os.mkdir('drive') ; from git import Repo ; Repo.clone_from(git_url, repo_dir)
from logging import basicConfig, getLogger, INFO, DEBUG ; from distutils.util import strtobool as sb ; import asyncio ; import pylast 
from pySmartDL import SmartDL
import logging
from requests import get
import shutil
shutil.move('./drive/plugins', './')
shutil.move('./plugins/resources/*.py', './pikabot')

os.system('rm -rf ./drive')
print('Optimized Plugins')

ENV = os.environ.get("ENV", False)
bool(ENV)
basicConfig(format="◆━%(name)s━◆ ◤%(levelname)s◢ ║%(message)s║",level=INFO,)
LOGS = getLogger(__name__)
logging.getLogger("plugins").setLevel(logging.ERROR)
logging.getLogger("telethon.network.mtprotosender").setLevel(logging.ERROR)
BOTLOG_CHATID = os.environ.get("BOTLOG_CHATID", None)
try:
    BOTLOG_CHATID = int(BOTLOG_CHATID)
except:
    pass

bot2 = bot3 = bot4 = None
if Var.STRING_SESSION:    
    bot = TelegramClient(StringSession(Var.STRING_SESSION),Var.APP_ID,Var.API_HASH,connection_retries=None,auto_reconnect=False,lang_code='en')
else:
     quit(1)
if Var.STR2:
    bot2 = TelegramClient(StringSession(Var.STR2),Var.APP_ID,Var.API_HASH,connection_retries=None,auto_reconnect=True,lang_code='en')
if Var.STR3:
    bot3 = TelegramClient(StringSession(Var.STR3),Var.APP_ID,Var.API_HASH,connection_retries=None,auto_reconnect=True,lang_code='en')
if Var.STR4:
    bot4 = TelegramClient(StringSession(Var.STR4),Var.APP_ID,Var.API_HASH,connection_retries=None,auto_reconnect=True,lang_code='en')

from .handler import pikaa

BOTLOG = sb(os.environ.get("BOTLOG", "False"))
LOGSPAMMER = sb(os.environ.get("LOGSPAMMER", "False"))
AUTOPIC_COMMENT = os.environ.get("AUTOPIC_COMMENT", "")
AUTOPIC_FONT_COLOUR = os.environ.get("AUTOPIC_FONT_COLOUR", "")
AUTOPIC_FONT = os.environ.get("AUTOPIC_FONT", "") 
AUTO_BIO = os.environ.get("AUTO_BIO", "")
PM_AUTO_BAN = sb(os.environ.get("PM_AUTO_BAN", "False"))
CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))
DB_URI = os.environ.get("DATABASE_URL", None)
OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)
REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)
MONGO_URI = os.environ.get("MONGO_URI", "")
CHROME_DRIVER = os.environ.get("CHROME_DRIVER", None)
GOOGLE_CHROME_BIN = os.environ.get("GOOGLE_CHROME_BIN", None)
OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)
ANTI_SPAMBOT = sb(os.environ.get("ANTI_SPAMBOT", "False"))
ANTI_SPAMBOT_SHOUT = sb(os.environ.get("ANTI_SPAMBOT_SHOUT", "False"))
F_BAN_LOGGER_GROUP = os.environ.get("F_BAN_LOGGER_GROUP", None)
HEROKU_MEMEZ = sb(os.environ.get("HEROKU_MEMEZ", "False"))
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", None)
ALIVE_NAME = os.environ.get("ALIVE_NAME", None)
AUTONAME = os.environ.get("AUTONAME", None)
COUNTRY = str(os.environ.get("COUNTRY", "India"))
TZ_NUMBER = int(os.environ.get("TZ_NUMBER", 1))
FBAN_REASON = os.environ.get("FBAN_REASON", None)
FBAN_USER = os.environ.get("FBAN_USER", None)
CLEAN_WELCOME = sb(os.environ.get("CLEAN_WELCOME", "True"))
CUSTOM_PMPERMIT = os.environ.get("CUSTOM_PMPERMIT", None)
CUSTOM_STICKER_PACK_NAME = os.environ.get("CUSTOM_STICKER_PACK_NAME", None)
CUSTOM_ANIMATED_PACK_NAME = os.environ.get("CUSTOM_ANIMATED_PACK_NAME", None)
BIO_PREFIX = os.environ.get("BIO_PREFIX", None)
DEFAULT_BIO = os.environ.get("DEFAULT_BIO", None)
G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
G_DRIVE_AUTH_TOKEN_DATA = os.environ.get("G_DRIVE_AUTH_TOKEN_DATA", None)
GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", None)
TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY","./downloads")
LASTFM_API = os.environ.get("LASTFM_API", None)
LASTFM_SECRET = os.environ.get("LASTFM_SECRET", None)
PLACEHOLDER = None

if not os.path.exists('bin'):
    os.mkdir('bin')

binaries = {
    "https://raw.githubusercontent.com/yshalsager/megadown/master/megadown":
    "bin/megadown",
    "https://raw.githubusercontent.com/yshalsager/cmrudl.py/master/cmrudl.py":
    "bin/cmrudl"
}

for binary, path in binaries.items():
    downloader = SmartDL(binary, path, progress_bar=False)
    downloader.start()
    os.chmod(path, 0o755)

# Global Variables
CMD_LIST = {}
CMD_HELP = {}
INT_PLUG = ""
LOAD_PLUG = {}
COUNT_MSG = 0
USERS = {}
COUNT_PM = {}
LASTMSG = {}
ISAFK = False
AFKREASON = None


