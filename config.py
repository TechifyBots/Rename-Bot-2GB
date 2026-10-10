import os, time, re
from typing import List
id_pattern = re.compile(r'^.\d+$')

class Config(object):
    API_ID = os.environ.get("API_ID", "")
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    DATABASE_NAME = os.environ.get("DATABASE_NAME","techifybots")     
    DATABASE_URL = os.environ.get("DATABASE_URL","")
    PICS = (os.environ.get("PICS", "https://i.ibb.co/MDssddJp/pic.jpg https://i.ibb.co/n8fQ2xcx/pic.jpg")).split()
    ADMIN = int(os.environ.get("ADMIN", ""))
    IS_FSUB = os.environ.get("IS_FSUB", "False").lower() == "true"  # Set "True" For Enable Force Subscribe
    AUTH_CHANNELS = list(map(int, os.environ.get("AUTH_CHANNELS", "").split())) # Add Multiple channel ids
    AUTH_REQ_CHANNELS = list(map(int, os.environ.get("AUTH_REQ_CHANNELS", "").split())) # Add Multiple channel ids
    FSUB_EXPIRE = int(os.environ.get("FSUB_EXPIRE", 2))  # minutes, 0 = no expiry
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))
    BIN_CHANNEL = int(os.environ.get("BIN_CHANNEL", ""))     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    BOT_UPTIME = time.time()
    PING_URL = os.environ.get("PING_URL", "") # Service URL for Keep-Alive
    VERSION = os.environ.get("VERSION", "3.0")


class Txt(object):
    START_TXT = """{},

𝖴𝗌𝗂𝗇𝗀 𝗍𝗁𝗂𝗌 𝖻𝗈𝗍 𝗒𝗈𝗎 𝖼𝖺𝗇 𝗋𝖾𝗇𝖺𝗆𝖾 𝖺𝗇𝖽 𝖼𝗁𝖺𝗇𝗀𝖾 𝗍𝗁𝗎𝗆𝖻𝗇𝖺𝗂𝗅 𝗈𝖿 𝗒𝗈𝗎𝗋 𝖿𝗂𝗅𝖾𝗌. 𝖠𝗇𝖽 𝗒𝗈𝗎 𝖼𝖺𝗇 𝖺𝗅𝗌𝗈 𝖼𝗈𝗇𝗏𝖾𝗋𝗍 𝗏𝗂𝖽𝖾𝗈 𝗍𝗈 𝖿𝗂𝗅𝖾 𝖺𝗇𝖽 𝖿𝗂𝗅𝖾 𝗍𝗈 𝗏𝗂𝖽𝖾𝗈.

<blockquote><b>𝘕𝘰𝘵𝘦 :</b> 𝘈𝘥𝘶𝘭𝘵 𝘊𝘰𝘯𝘵𝘦𝘯𝘵 𝘪𝘴 𝘚𝘛𝘙𝘐𝘊𝘛𝘓𝘠 𝘱𝘳𝘰𝘩𝘪𝘣𝘪𝘵𝘦𝘥 𝘉𝘢𝘯 𝘸𝘪𝘭𝘭 𝘣𝘦 𝘱𝘦𝘳𝘮𝘢𝘯𝘦𝘯𝘵.</blockquote>"""

    ABOUT_TXT = """<blockquote>🤖 𝗕𝗼𝘁 𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻</blockquote>

<b>‣ 𝖬𝗒 𝖭𝖺𝗆𝖾 :</b> <a href='https://youtube.com/@techifybots'>𝖳𝖾𝖼𝗁𝗂𝖿𝗒 𝖡𝗈𝗍𝗌</a>
<b>‣ 𝖵𝖾𝗋𝗌𝗂𝗈𝗇 :</b> v{}
<b>‣ 𝖫𝗂𝖻𝗋𝖺𝗋𝗒 :</b> <a href='https://docs.pyrogram.org/'>𝖯𝗒𝗋𝗈𝗀𝗋𝖺𝗆</a>
<b>‣ 𝖣𝖺𝗍𝖺𝖻𝖺𝗌𝖾 :</b> <a href='https://www.mongodb.com/'>𝖬𝗈𝗇𝗀𝗈𝖣𝖡</a>
<b>‣ 𝖫𝖺𝗇𝗀𝗎𝖺𝗀𝖾 :</b> <a href='https://www.python.org/download/releases/3.0/'>𝖯𝗒𝗍𝗁𝗈𝗇 𝟹</a>
<b>‣ 𝖡𝗈𝗍 𝖲𝖾𝗋𝗏𝖾𝗋 :</b> <a href='https://www.koyeb.com/'>𝖪𝗈𝗒𝖾𝖻</a>
<b>‣ 𝖢𝗋𝖾𝖺𝗍𝖾𝖽 𝖡𝗒 :</b> <a href='https://telegram.me/callownerbot'>𝖱𝖺𝗁𝗎𝗅</a>"""

    GUIDE_TXT = """<blockquote>❓ 𝗛𝗮𝘃𝗶𝗻𝗴 𝗧𝗿𝗼𝘂𝗯𝗹𝗲?</blockquote>

𝖨𝖿 𝗒𝗈𝗎'𝗋𝖾 𝖿𝖺𝖼𝗂𝗇𝗀 𝖺𝗇𝗒 𝗉𝗋𝗈𝖻𝗅𝖾𝗆 𝗐𝗁𝗂𝗅𝖾 𝗎𝗌𝗂𝗇𝗀 𝗍𝗁𝖾 𝖻𝗈𝗍 𝗈𝗋 𝗂𝗍𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽𝗌, 𝗉𝗅𝖾𝖺𝗌𝖾 𝗐𝖺𝗍𝖼𝗁 𝗍𝗁𝖾 𝗍𝗎𝗍𝗈𝗋𝗂𝖺𝗅 𝗏𝗂𝖽𝖾𝗈 𝖻𝖾𝗅𝗈𝗐.

🎥 𝖳𝗁𝖾 𝗏𝗂𝖽𝖾𝗈 𝗐𝗂𝗅𝗅 𝖼𝗅𝖾𝖺𝗋𝗅𝗒 𝖾𝗑𝗉𝗅𝖺𝗂𝗇 𝗁𝗈𝗐 𝗍𝗈 𝗎𝗌𝖾 𝖾𝖺𝖼𝗁 𝖿𝖾𝖺𝗍𝗎𝗋𝖾 𝗐𝗂𝗍𝗁 𝖾𝖺𝗌𝖾.

<blockquote><i>💖 𝖥𝗈𝗋 𝗆𝗈𝗋𝖾 𝗎𝗉𝖽𝖺𝗍𝖾𝗌 — <b><a href='https://techifybots.vercel.app/pay'>𝖲𝗎𝗉𝗉𝗈𝗋𝗍 𝖴𝗌</a></b></i></blockquote>"""

    HELP_TXT = """𝖱𝖾𝗇𝖺𝗆𝖾 𝖡𝗈𝗍 𝖨𝗌 𝖠 𝖧𝖺𝗇𝖽𝗒 𝖳𝗈𝗈𝗅 𝖳𝗁𝖺𝗍 𝖧𝖾𝗅𝗉𝗌 𝖸𝗈𝗎 𝖱𝖾𝗇𝖺𝗆𝖾 𝖠𝗇𝖽 𝖬𝖺𝗇𝖺𝗀𝖾 𝖸𝗈𝗎𝗋 𝖥𝗂𝗅𝖾𝗌 𝖤𝖿𝖿𝗈𝗋𝗍𝗅𝖾𝗌𝗌𝗅𝗒.

➻ 𝖢𝗅𝗂𝖼𝗄 𝖮𝗇 𝖳𝗁𝖾 𝖡𝗎𝗍𝗍𝗈𝗇𝗌 𝖦𝗂𝗏𝖾𝗇 𝖡𝖾𝗅𝗈𝗐 𝖥𝗈𝗋 𝖦𝖾𝗍𝗍𝗂𝗇𝗀 𝖬𝗈𝗋𝖾 𝖨𝗇𝖿𝗈."""

    THUMBNAIL_TXT = """<blockquote>🖼 𝖳𝗈 𝖲𝖾𝗍 𝖢𝗎𝗌𝗍𝗈𝗆 𝖳𝗁𝗎𝗆𝖻𝗇𝖺𝗂𝗅</blockquote>

➲ 𝖲𝖾𝗇𝖽 𝖠𝗇𝗒 𝖯𝗁𝗈𝗍𝗈 𝖳𝗈 𝖠𝗎𝗍𝗈𝗆𝖺𝗍𝗂𝖼𝖺𝗅𝗅𝗒 𝖲𝖾𝗍 𝖨𝗍 𝖠𝗌 𝖠 𝖳𝗁𝗎𝗆𝖻𝗇𝖺𝗂𝗅.  
➲ /delthumb: 𝖴𝗌𝖾 𝖳𝗁𝗂𝗌 𝖢𝗈𝗆𝗆𝖺𝗇𝖽 𝖳𝗈 𝖣𝖾𝗅𝖾𝗍𝖾 𝖸𝗈𝗎𝗋 𝖳𝗁𝗎𝗆𝖻𝗇𝖺𝗂𝗅.  
➲ /viewthumb: 𝖴𝗌𝖾 𝖳𝗁𝗂𝗌 𝖢𝗈𝗆𝗆𝖺𝗇𝖽 𝖳𝗈 𝖵𝗂𝖾𝗐 𝖸𝗈𝗎𝗋 𝖢𝗎𝗋𝗋𝖾𝗇𝗍 𝖳𝗁𝗎𝗆𝖻𝗇𝖺𝗂𝗅.

<b>𝖭𝗈𝗍𝖾 :</b> 𝖨𝖿 𝖭𝗈 𝖳𝗁𝗎𝗆𝖻𝗇𝖺𝗂𝗅 𝖲𝖺𝗏𝖾𝖽 𝖨𝗇 𝖡𝗈𝗍 𝖳𝗁𝖾𝗇, 𝖨𝗍 𝖶𝗂𝗅𝗅 𝖴𝗌𝖾 𝖳𝗁𝗎𝗆𝖻𝗇𝖺𝗂𝗅 𝖮𝖿 𝖳𝗁𝖾 𝖮𝗋𝗂𝗀𝗂𝗇𝖺𝗅 𝖥𝗂𝗅𝖾 𝖳𝗈 𝖲𝖾𝗍 𝖨𝗇 𝖱𝖾𝗇𝖺𝗆𝖾𝖽 𝖥𝗂𝗅𝖾."""

    CAPTION_TXT = """<blockquote>📝 𝖳𝗈 𝖲𝖾𝗍 𝖢𝗎𝗌𝗍𝗈𝗆 𝖢𝖺𝗉𝗍𝗂𝗈𝗇 𝖠𝗇𝖽 𝖬𝖾𝖽𝗂𝖺 𝖳𝗒𝗉𝖾</blockquote>

<b>𝖵𝖺𝗋𝗂𝖺𝖻𝗅𝖾𝗌 :</b>         
𝖲𝗂𝗓𝖾: {filesize}  
𝖣𝗎𝗋𝖺𝗍𝗂𝗈𝗇: {duration}  
𝖥𝗂𝗅𝖾𝗇𝖺𝗆𝖾: {filename}

➲ /setcaption: 𝖳𝗈 𝖲𝖾𝗍 𝖠 𝖢𝗎𝗌𝗍𝗈𝗆 𝖢𝖺𝗉𝗍𝗂𝗈𝗇.  
➲ /seecaption: 𝖳𝗈 𝖵𝗂𝖾𝗐 𝖸𝗈𝗎𝗋 𝖢𝗎𝗌𝗍𝗈𝗆 𝖢𝖺𝗉𝗍𝗂𝗈𝗇.  
➲ /delcaption: 𝖳𝗈 𝖣𝖾𝗅𝖾𝗍𝖾 𝖸𝗈𝗎𝗋 𝖢𝗎𝗌𝗍𝗈𝗆 𝖢𝖺𝗉𝗍𝗂𝗈𝗇.

» 𝖤𝗑: /setcaption 𝖥𝗂𝗅𝖾 𝖭𝖺𝗆𝖾: {filename}"""

    PREFIX = """<blockquote>📜 𝖳𝗈 𝖲𝖾𝗍 𝖢𝗎𝗌𝗍𝗈𝗆 𝖯𝗋𝖾𝖿𝗂𝗑</blockquote>

➲ /setprefix: 𝖳𝗈 𝖲𝖾𝗍 𝖠 𝖢𝗎𝗌𝗍𝗈𝗆 𝖯𝗋𝖾𝖿𝗂𝗑.  
➲ /seeprefix: 𝖳𝗈 𝖵𝗂𝖾𝗐 𝖸𝗈𝗎𝗋 𝖢𝗎𝗌𝗍𝗈𝗆 𝖯𝗋𝖾𝖿𝗂𝗑.  
➲ /delprefix: 𝖳𝗈 𝖣𝖾𝗅𝖾𝗍𝖾 𝖸𝗈𝗎𝗋 𝖢𝗎𝗌𝗍𝗈𝗆 𝖯𝗋𝖾𝖿𝗂𝗑.

» 𝖤𝗑: `/setprefix @TechifyBots`"""

    SUFFIX = """<blockquote>📜 𝖳𝗈 𝖲𝖾𝗍 𝖢𝗎𝗌𝗍𝗈𝗆 𝖲𝗎𝖿𝖿𝗂𝗑</blockquote>

➲ /setsuffix: 𝖳𝗈 𝖲𝖾𝗍 𝖠 𝖢𝗎𝗌𝗍𝗈𝗆 𝖲𝗎𝖿𝖿𝗂𝗑.  
➲ /seesuffix: 𝖳𝗈 𝖵𝗂𝖾𝗐 𝖸𝗈𝗎𝗋 𝖢𝗎𝗌𝗍𝗈𝗆 𝖲𝗎𝖿𝖿𝗂𝗑.  
➲ /delsuffix: 𝖳𝗈 𝖣𝖾𝗅𝖾𝗍𝖾 𝖸𝗈𝗎𝗋 𝖢𝗎𝗌𝗍𝗈𝗆 𝖲𝗎𝖿𝖿𝗂𝗑.

» 𝖤𝗑: `/setsuffix @TechifyBots`"""

    PROGRESS_BAR = """\n
<b>😶‍🌫 𝖲𝗂𝗓𝖾 :</b> {1} | {2}
<b>⏳️ 𝖣𝗈𝗇𝖾 :</b> {0}%
<b>🚀 𝖲𝗉𝖾𝖾𝖽 :</b> {3}/s
<b>⏰️ 𝖤𝖳𝖠 :</b> {4}
"""

    DONATE_TXT = """<blockquote>☕ 𝗦𝘂𝗽𝗽𝗼𝗿𝘁 𝗧𝗵𝗲 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿</blockquote>

𝖪𝖾𝖾𝗉𝗂𝗇𝗀 𝗍𝗁𝗂𝗌 𝖻𝗈𝗍 𝖿𝖺𝗌𝗍 𝖺𝗇𝖽 𝗈𝗇𝗅𝗂𝗇𝖾 𝟤𝟦/𝟩 𝗋𝖾𝗊𝗎𝗂𝗋𝖾𝗌 𝗌𝖾𝗋𝗏𝖾𝗋 𝗋𝖾𝗌𝗈𝗎𝗋𝖼𝖾𝗌. 𝖨𝖿 𝗒𝗈𝗎 𝖾𝗇𝗃𝗈𝗒 𝗎𝗌𝗂𝗇𝗀 𝗍𝗁𝗂𝗌 𝖻𝗈𝗍, 𝖼𝗈𝗇𝗌𝗂𝖽𝖾𝗋 𝖿𝗎𝖾𝗅𝗂𝗇𝗀 𝗂𝗍𝗌 𝖽𝖾𝗏𝖾𝗅𝗈𝗉𝗆𝖾𝗇𝗍! ✨

💳 <b>𝖴𝖯𝖨 𝖨𝖣:</b> <code>RahulDhankhar@UPI</code>

<blockquote><i>𝖤𝗏𝖾𝗋𝗒 𝖼𝗈𝗇𝗍𝗋𝗂𝖻𝗎𝗍𝗂𝗈𝗇 𝗄𝖾𝖾𝗉𝗌 𝗍𝗁𝖾 𝗌𝖾𝗋𝗏𝖾𝗋𝗌 𝗁𝗎𝗆𝗆𝗂𝗇𝗀. 𝖳𝗁𝖺𝗇𝗄 𝗒𝗈𝗎! 💖</i></blockquote>"""

    SEND_METADATA = """<blockquote>📝 𝖳𝗈 𝖲𝖾𝗍 𝖢𝗎𝗌𝗍𝗈𝗆 𝖬𝖾𝗍𝖺𝖽𝖺𝗍𝖺</blockquote>

➲ /metadata: 𝖳𝗈 𝖲𝖾𝗍 𝖠 𝖢𝗎𝗌𝗍𝗈𝗆 𝖬𝖾𝗍𝖺𝖽𝖺𝗍𝖺

𝖠𝖿𝗍𝖾𝗋 𝖴𝗌𝗂𝗇𝗀 𝖢𝗆𝖽 𝖲𝖾𝗇𝖽 𝖠𝗇𝗒 𝖳𝖾𝗑𝗍 𝖨 𝖶𝗂𝗅𝗅 𝖲𝖺𝗏𝖾 𝖨𝗍 𝖠𝗌 𝖸𝗈𝗎𝗋 𝖬𝖾𝗍𝖺𝖽𝖺𝗍𝖺

» 𝖤𝗑: `@TechifyBots`"""
