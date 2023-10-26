#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("API_ID", "22046086", default=None, cast=int)
API_HASH = config("API_HASH", "ff5490575199fefa4bee702dc389bbe4", default=None)
BOT_TOKEN = config("BOT_TOKEN", "6811875648:AAER8ABArCB0lDbtKppkYMJzAoYFxYzZHv4", default=None)
SESSION = config("SESSION", "BQBXMacnGtWjvEVpOPkqtpBjHI4NLwL0QGm9BYoYC8ym_HL01kD3j7xug2h01nnua35mJC4mtHMGN373goW3ldTorE2yy45Gf2IXbLhC_R0ljQQ5LtdHj0cQLnTfBwIG6OILz2NLQ6nlKfkmNIpMbh4Xfti7dosMtb3wNSiON4BovmpUGrQpw8dY-oVExOlXbLaAFh7CxrlkITvdHo5L67XUc_0VAL32b3nRYQr-clilaJqVOdTI1XH6xJRuTSsn-Y_cxNylGACfcLBNIi51x8E55CaAN0sxyaBmhhEJhHSlUC5Xh6H9KYwYXuPvsIXwg3Gby2zZpTcg-ns6lNPBlYdcMYep1QA", default=None)
FORCESUB = config("FORCESUB", default=None)
AUTH = config("AUTH", "830974421", default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
