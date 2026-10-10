import os
import sys
import time
import asyncio
import logging
import datetime
from config import Config
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pyrogram.errors import FloodWait, InputUserDeactivated, UserIsBlocked, PeerIdInvalid
from .database import tb

logger=logging.getLogger(__name__)
logger.setLevel(logging.INFO)

@Client.on_message(filters.command("status") & filters.user(Config.ADMIN))
async def get_stats(bot,message):
    total_users=await tb.total_users_count()
    uptime=time.strftime("%Hh%Mm%Ss",time.gmtime(time.time()-bot.uptime))
    start_t=time.time()
    st=await message.reply('**Processing The Details.....**',quote=True)
    end_t=time.time()
    time_taken_s=(end_t-start_t)*1000
    await st.edit(text=f"**--Bot Stats--** \n\n**⌚ Bot Uptime:** `{uptime}` \n**🐌 Current Ping:** `{time_taken_s:.3f} ms` \n**👭 Total Users:** `{total_users}`")

@Client.on_message(filters.command("restart") & filters.user(Config.ADMIN))
async def restart_bot(bot,message):
    msg=await bot.send_message(text="🔄 Processes Stoped. Bot Is Restarting...",chat_id=message.chat.id)
    await asyncio.sleep(3)
    await msg.edit("✅️ Bot Is Restarted. Now You Can Use Me")
    os.execl(sys.executable,sys.executable,*sys.argv)

@Client.on_message(filters.private & filters.command("ping"))
async def ping(_,message):
    start_t=time.time()
    rm=await message.reply_text("Pinging....",quote=True)
    end_t=time.time()
    time_taken_s=(end_t-start_t)*1000
    await rm.edit(f"Ping 🔥!\n{time_taken_s:.3f} ms")

@Client.on_message(filters.command("broadcast") & filters.user(Config.ADMIN) & filters.reply)
async def broadcast_handler(bot:Client,m:Message):
    await bot.send_message(Config.LOG_CHANNEL,f"{m.from_user.mention} or {m.from_user.id} Is Started The Broadcast......")
    all_users=await tb.get_all_users()
    broadcast_msg=m.reply_to_message
    sts_msg=await m.reply_text("Broadcast Started..!",quote=True)
    done=0
    failed=0
    success=0
    start_time=time.time()
    total_users=await tb.total_users_count()
    async for user in all_users:
        sts=await send_msg(user['_id'],broadcast_msg)
        if sts==200:
            success+=1
        else:
            failed+=1
        if sts==400:
            await tb.delete_user(user['_id'])
        done+=1
        if not done%20:
            await sts_msg.edit(f"**Broadcast In Progress:** \n\nTotal Users {total_users} \nCompleted: {done} / {total_users}\nSuccess: {success}\nFailed: {failed}")
    completed_in=datetime.timedelta(seconds=int(time.time()-start_time))
    await sts_msg.edit(f"**Broadcast Completed:** \n\nCompleted In `{completed_in}`.\n\nTotal Users {total_users}\nCompleted: {done} / {total_users}\nSuccess: {success}\nFailed: {failed}")

async def send_msg(user_id,message):
    try:
        await message.copy(chat_id=int(user_id))
        return 200
    except FloodWait as e:
        await asyncio.sleep(e.value)
        return send_msg(user_id,message)
    except InputUserDeactivated:
        logger.info(f"{user_id} : Deactivated")
        return 400
    except UserIsBlocked:
        logger.info(f"{user_id} : Blocked The Bot")
        return 400
    except PeerIdInvalid:
        logger.info(f"{user_id} : User ID Invalid")
        return 400
    except Exception as e:
        logger.error(f"{user_id} : {e}")
        return 500

@Client.on_message(filters.command("banned") & filters.user(Config.ADMIN))
async def banned_users(client,message):
    users=await tb.bannedList.find().to_list(None)
    if not users:
        return await message.reply_text("No users are currently banned.")
    text="🚫 Banned Users:\n\n"
    for u in users:
        text+=f"{u['banId']}\n"
    if len(text)<=4000:
        return await message.reply_text(text)
    await client.send_document(message.chat.id,text.encode(),file_name="banned_users.txt")

@Client.on_message(filters.command('ban') & filters.user(Config.ADMIN))
async def do_ban(bot,message):
    userid=message.text.split(" ",2)[1] if len(message.text.split(" ",1))>1 else None
    reason=message.text.split(" ",2)[2] if len(message.text.split(" ",2))>2 else None
    if not userid:
        return await message.reply('<b>ᴘʟᴇᴀsᴇ ᴀᴅᴅ ᴀ ᴠᴀʟɪᴅ ᴜsᴇʀ/ᴄʜᴀɴɴᴇʟ ɪᴅ</b>')
    text=await message.reply("<b>ʟᴇᴛ ᴍᴇ ᴄʜᴇᴄᴋ 👀</b>")
    banSts=await tb.ban_user(userid)
    if banSts==True:
        await text.edit(text=f"<b><code>{userid}</code> ʜᴀs ʙᴇᴇɴ ʙᴀɴɴᴇᴅ</b>",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("ʏᴇs ✅",callback_data=f"sendAlert_{userid}_{reason if reason else 'no reason provided'}"),InlineKeyboardButton("ɴᴏ ❌",callback_data=f"noAlert_{userid}")]]))
    else:
        await text.edit(f"<b><code>{userid}</code> ɪs ᴀʟʀᴇᴀᴅʏ ʙᴀɴɴᴇᴅ</b>")

@Client.on_message(filters.command('unban') & filters.user(Config.ADMIN))
async def do_unban(bot,message):
    userid=message.text.split(" ",2)[1] if len(message.text.split(" ",1))>1 else None
    if not userid:
        return await message.reply('ɢɪᴠᴇ ᴍᴇ ᴀɴ ɪᴅ\nᴇx : <code>/unban 1234567899</code>')
    text=await message.reply("<b>ʟᴇᴛ ᴍᴇ ᴄʜᴇᴄᴋ 🥱</b>")
    unban_chk=await tb.is_unbanned(userid)
    if unban_chk==True:
        await text.edit(text=f'<b><code>{userid}</code> ɪs ᴜɴʙᴀɴɴᴇᴅ</b>',reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("ʏᴇs ✅",callback_data=f"sendUnbanAlert_{userid}"),InlineKeyboardButton("ɴᴏ ❌",callback_data=f"NoUnbanAlert_{userid}")]]))
    elif unban_chk==False:
        await text.edit('<b>ᴜsᴇʀ ɪs ɴᴏᴛ ʙᴀɴɴᴇᴅ ʏᴇᴛ.</b>')
    else:
        await text.edit(f"<b>ғᴀɪʟᴇᴅ ᴛᴏ ᴜɴʙᴀɴ.\nʀᴇᴀsᴏɴ : {unban_chk}</b>")
