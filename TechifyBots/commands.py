import random
import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, InputMediaPhoto
from .database import tb
from config import Config, Txt  

@Client.on_message(filters.private & filters.command("start"))
async def start(client, message):
    user = message.from_user
    await tb.add_user(client, message)
    button = InlineKeyboardMarkup([
        [InlineKeyboardButton('ℹ️ 𝖠𝖻𝗈𝗎𝗍', callback_data='about'),
         InlineKeyboardButton('📚 𝖧𝖾𝗅𝗉', callback_data='help')],
        [InlineKeyboardButton('👨‍💻 𝖣𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝗋', user_id=int(Config.ADMIN))]
    ])
    await message.reply_photo(
        photo=random.choice(Config.PICS),
        caption=Txt.START_TXT.format(user.mention),
        reply_markup=button
    )

@Client.on_message(filters.private & filters.command("help"))
async def help_cmd(client, message):
    msg = await message.reply(Txt.GUIDE_TXT,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🎬 𝖶𝖺𝗍𝖼𝗁 𝖳𝗎𝗍𝗈𝗋𝗂𝖺𝗅", url="https://youtu.be/6BWLUL3Faxs")]])
    )
    await asyncio.sleep(300)
    try:
        await msg.delete()
        await message.delete()
    except Exception:
        pass

@Client.on_message(filters.private & filters.command('setcaption'))
async def add_caption(client,message):
    if len(message.command)==1:
        return await message.reply_text("**Give The Caption\n\nExample :- `/setcaption 📕Name ➠ : {filename}\n\n🔗 Size ➠ : {filesize}\n\n⏰ Duration ➠ : {duration}`**",quote=True)
    caption=message.text.split(" ",1)[1]
    await tb.set_caption(message.from_user.id,caption=caption)
    await message.reply_text("**Your Caption Successfully Added ✅**",quote=True)

@Client.on_message(filters.private & filters.command('delcaption'))
async def delete_caption(client,message):
    caption=await tb.get_caption(message.from_user.id)
    if not caption:
        return await message.reply_text("**You Don't Have Any Caption ❌**",quote=True)
    await tb.set_caption(message.from_user.id,caption=None)
    await message.reply_text("**Your Caption Successfully Deleted 🗑️**",quote=True)

@Client.on_message(filters.private & filters.command('seecaption'))
async def see_caption(client,message):
    caption=await tb.get_caption(message.from_user.id)
    if caption:
        await message.reply_text(f"**Your Caption :**\n\n`{caption}`",quote=True)
    else:
        await message.reply_text("**You Don't Have Any Caption ❌**",quote=True)

@Client.on_message(filters.private & filters.command('viewthumb'))
async def viewthumb(client,message):
    thumb=await tb.get_thumbnail(message.from_user.id)
    if thumb:
        sent_msg=await client.send_photo(chat_id=message.chat.id,photo=thumb)
    else:
        sent_msg=await message.reply_text("❌ **𝖸𝗈𝗎 𝖣𝗈𝗇'𝗍 𝖧𝖺𝗏𝖾 𝖠𝗇𝗒 𝖳𝗁𝗎𝗆𝖻𝗇𝖺𝗂𝗅**",quote=True)
    await asyncio.sleep(30)
    await sent_msg.delete()
    await message.delete()

@Client.on_message(filters.private & filters.command('delthumb'))
async def removethumb(client,message):
    await tb.set_thumbnail(message.from_user.id,file_id=None)
    await message.reply_text("🗑️ **𝖳𝗁𝗎𝗆𝖻𝗇𝖺𝗂𝗅 𝖣𝖾𝗅𝖾𝗍𝖾𝖽 𝖲𝗎𝖼𝖼𝖾𝗌𝗌𝖿𝗎𝗅𝗅𝗒**",quote=True)

@Client.on_message(filters.private & filters.photo)
async def addthumbs(client,message):
    rd=await message.reply_text("⏳ **𝖯𝗅𝖾𝖺𝗌𝖾 𝖶𝖺𝗂𝗍...**",quote=True)
    await tb.set_thumbnail(message.from_user.id,file_id=message.photo.file_id)
    await rd.edit("✅ **𝖳𝗁𝗎𝗆𝖻𝗇𝖺𝗂𝗅 𝖲𝖺𝗏𝖾𝖽 𝖲𝗎𝖼𝖼𝖾𝗌𝗌𝖿𝗎𝗅𝗅𝗒**")
    await asyncio.sleep(30)
    await message.delete()
    await rd.delete()

@Client.on_message(filters.private & filters.command('setprefix'))
async def add_prefix(client,message):
    if len(message.command)==1:
        return await message.reply_text("**Give The Prefix**\n\nExample:- `/setprefix @TechifyBots`",quote=True)
    prefix=message.text.split(" ",1)[1]
    m=await message.reply_text("Please Wait ...",quote=True)
    await tb.set_prefix(message.from_user.id,prefix)
    await m.edit("**Prefix Saved Successfully ✅**")

@Client.on_message(filters.private & filters.command('delprefix'))
async def delete_prefix(client,message):
    m=await message.reply_text("Please Wait ...",quote=True)
    prefix=await tb.get_prefix(message.from_user.id)
    if not prefix:
        return await m.edit("**You Don't Have Any Prefix ❌**")
    await tb.set_prefix(message.from_user.id,None)
    await m.edit("**Prefix Deleted Successfully 🗑️**")

@Client.on_message(filters.private & filters.command('seeprefix'))
async def see_prefix(client,message):
    m=await message.reply_text("Please Wait ...",quote=True)
    prefix=await tb.get_prefix(message.from_user.id)
    if prefix:
        await m.edit(f"**Your Prefix :-**\n\n`{prefix}`")
    else:
        await m.edit("**You Don't Have Any Prefix ❌**")

@Client.on_message(filters.private & filters.command('setsuffix'))
async def add_suffix(client,message):
    if len(message.command)==1:
        return await message.reply_text("**Give The Suffix**\n\nExample:- `/setsuffix @TechifyBots`",quote=True)
    suffix=message.text.split(" ",1)[1]
    m=await message.reply_text("Please Wait ...",quote=True)
    await tb.set_suffix(message.from_user.id,suffix)
    await m.edit("**Suffix Saved Successfully ✅**")

@Client.on_message(filters.private & filters.command('delsuffix'))
async def delete_suffix(client,message):
    m=await message.reply_text("Please Wait ...",quote=True)
    suffix=await tb.get_suffix(message.from_user.id)
    if not suffix:
        return await m.edit("**You Don't Have Any Suffix ❌**")
    await tb.set_suffix(message.from_user.id,None)
    await m.edit("**Suffix Deleted Successfully 🗑️**")

@Client.on_message(filters.private & filters.command('seesuffix'))
async def see_suffix(client,message):
    m=await message.reply_text("Please Wait ...",quote=True)
    suffix=await tb.get_suffix(message.from_user.id)
    if suffix:
        await m.edit(f"**Your Suffix :-**\n\n`{suffix}`")
    else:
        await m.edit("**You Don't Have Any Suffix ❌**")

@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data 

    if data == "start":
        await query.message.edit_media(
            media=InputMediaPhoto(
                random.choice(Config.PICS),
                caption=Txt.START_TXT.format(query.from_user.mention)
            ),
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton('ℹ️ 𝖠𝖻𝗈𝗎𝗍', callback_data='about'),
                 InlineKeyboardButton('📚 𝖧𝖾𝗅𝗉', callback_data='help')],
                [InlineKeyboardButton('👨‍💻 𝖣𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝗋', user_id=int(Config.ADMIN))]
            ])
        )

    elif data == "help":
        await query.message.edit_media(
            media=InputMediaPhoto(
                random.choice(Config.PICS),
                caption=Txt.HELP_TXT
            ),
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🧬 𝖲𝖾𝗍 𝖬𝖾𝗍𝖺𝖽𝖺𝗍𝖺", callback_data="meta")],
                [InlineKeyboardButton("🔤 𝖯𝗋𝖾𝖿𝗂𝗑", callback_data="prefix"),
                 InlineKeyboardButton("🔤 𝖲𝗎𝖿𝖿𝗂𝗑", callback_data="suffix")],
                [InlineKeyboardButton("📝 𝖢𝖺𝗉𝗍𝗂𝗈𝗇", callback_data="caption"),
                 InlineKeyboardButton("🖼️ 𝖳𝗁𝗎𝗆𝖻𝗇𝖺𝗂𝗅", callback_data="thumbnail")],
                [InlineKeyboardButton("🏠 𝖧𝗈𝗆𝖾", callback_data="start")]
            ])
        )

    elif data == "meta":
        await query.message.edit_media(
            media=InputMediaPhoto(
                random.choice(Config.PICS),
                caption=Txt.SEND_METADATA
            ),
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 𝖡𝖺𝖼𝗄", callback_data="help"),
                 InlineKeyboardButton("❌ 𝖢𝗅𝗈𝗌𝖾", callback_data="close")]
            ])
        )

    elif data == "prefix":
        await query.message.edit_media(
            media=InputMediaPhoto(
                random.choice(Config.PICS),
                caption=Txt.PREFIX
            ),
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 𝖡𝖺𝖼𝗄", callback_data="help"),
                 InlineKeyboardButton("❌ 𝖢𝗅𝗈𝗌𝖾", callback_data="close")]
            ])
        )

    elif data == "suffix":
        await query.message.edit_media(
            media=InputMediaPhoto(
                random.choice(Config.PICS),
                caption=Txt.SUFFIX
            ),
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 𝖡𝖺𝖼𝗄", callback_data="help"),
                 InlineKeyboardButton("❌ 𝖢𝗅𝗈𝗌𝖾", callback_data="close")]
            ])
        )

    elif data == "caption":
        await query.message.edit_media(
            media=InputMediaPhoto(
                random.choice(Config.PICS),
                caption=Txt.CAPTION_TXT
            ),
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 𝖡𝖺𝖼𝗄", callback_data="help"),
                 InlineKeyboardButton("❌ 𝖢𝗅𝗈𝗌𝖾", callback_data="close")]
            ])
        )

    elif data == "thumbnail":
        await query.message.edit_media(
            media=InputMediaPhoto(
                random.choice(Config.PICS),
                caption=Txt.THUMBNAIL_TXT
            ),
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 𝖡𝖺𝖼𝗄", callback_data="help"),
                 InlineKeyboardButton("❌ 𝖢𝗅𝗈𝗌𝖾", callback_data="close")]
            ])
        )

    elif data == "about":
        await query.message.edit_media(
            media=InputMediaPhoto(
                random.choice(Config.PICS),
                caption=Txt.ABOUT_TXT
            ),
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("💻 𝖱𝖾𝗉𝗈", url="https://github.com/TechifyBots/Rename-Bot-2GB"),
                 InlineKeyboardButton("💖 𝖣𝗈𝗇𝖺𝗍𝖾", callback_data="donate")],
                [InlineKeyboardButton("🏠 𝖧𝗈𝗆𝖾", callback_data="start")]
            ])
        )

    elif data == "donate":
        await query.message.edit_media(
            media=InputMediaPhoto(
                random.choice(Config.PICS),
                caption=Txt.DONATE_TXT
            ),
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🤖 𝖬𝗈𝗋𝖾 𝖡𝗈𝗍𝗌", url="https://telegram.me/TechifyBots/8")],
                [InlineKeyboardButton("🔙 𝖡𝖺𝖼𝗄", callback_data="about"),
                 InlineKeyboardButton("❌ 𝖢𝗅𝗈𝗌𝖾", callback_data="close")]
            ])
        )

    elif data == "close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
            await query.message.continue_propagation()
        except:
            await query.message.delete()
            await query.message.continue_propagation()

    elif data.startswith("sendAlert"):
        user_id =(data.split("_")[1])
        user_id = int(user_id.replace(' ' , ''))
        if len(str(user_id)) == 10:
            reason = str(data.split("_")[2])
            try:
                await client.send_message(user_id , f"<b>ʏᴏᴜ ᴀʀᴇ ʙᴀɴɴᴇᴅ ʙʏ [ʀᴀʜᴜʟ](https://telegram.me/callownerbot)\nʀᴇᴀsᴏɴ : {reason}</b>")
                await query.message.edit(f"<b>Aʟᴇʀᴛ sᴇɴᴛ ᴛᴏ <code>{user_id}</code>\nʀᴇᴀsᴏɴ : {reason}</b>")
            except Exception as e:
                await query.message.edit(f"<b>sʀʏ ɪ ɢᴏᴛ ᴛʜɪs ᴇʀʀᴏʀ : {e}</b>")
        else:
            await query.message.edit(f"<b>Tʜᴇ ᴘʀᴏᴄᴇss ᴡᴀs ɴᴏᴛ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ʙᴇᴄᴀᴜsᴇ ᴛʜᴇ ᴜsᴇʀ ɪᴅ ᴡᴀs ɴᴏᴛ ᴠᴀʟɪᴅ, ᴏʀ ᴘᴇʀʜᴀᴘs ɪᴛ ᴡᴀs ᴀ ᴄʜᴀɴɴᴇʟ ɪᴅ</b>")

    elif data.startswith('noAlert'):
        user_id =(data.split("_")[1])
        user_id = int(user_id.replace(' ' , ''))
        await query.message.edit(f"<b>Tʜᴇ ʙᴀɴ ᴏɴ <code>{user_id}</code> ᴡᴀs ᴇxᴇᴄᴜᴛᴇᴅ sɪʟᴇɴᴛʟʏ.</b>")

    elif data.startswith('sendUnbanAlert'):
        user_id =(data.split("_")[1])
        user_id = int(user_id.replace(' ' , ''))
        if len(str(user_id)) == 10:
            try:
                unban_text = "<b>ʜᴜʀʀᴀʏ..ʏᴏᴜ ᴀʀᴇ ᴜɴʙᴀɴɴᴇᴅ ʙʏ [ʀᴀʜᴜʟ](https://telegram.me/callownerbot)</b>"
                await client.send_message(user_id , unban_text)
                await query.message.edit(f"<b>Uɴʙᴀɴɴᴇᴅ Aʟᴇʀᴛ sᴇɴᴛ ᴛᴏ <code>{user_id}</code>\nᴀʟᴇʀᴛ ᴛᴇxᴛ : {unban_text}</b>")
            except Exception as e:
                await query.message.edit(f"<b>sʀʏ ɪ ɢᴏᴛ ᴛʜɪs ᴇʀʀᴏʀ : {e}</b>")
        else:
            await query.message.edit(f"<b>Tʜᴇ ᴘʀᴏᴄᴇss ᴡᴀs ɴᴏᴛ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ʙᴇᴄᴀᴜsᴇ ᴛʜᴇ ᴜsᴇʀ ɪᴅ ᴡᴀs ɴᴏᴛ ᴠᴀʟɪᴅ, ᴏʀ ᴘᴇʀʜᴀᴘs ɪᴛ ᴡᴀs ᴀ ᴄʜᴀɴɴᴇʟ ɪᴅ</b>")

    elif data.startswith('NoUnbanAlert'):
        user_id =(data.split("_")[1])
        user_id = int(user_id.replace(' ' , ''))
        await query.message.edit(f"Tʜᴇ ᴜɴʙᴀɴ ᴏɴ <code>{user_id}</code> ᴡᴀs ᴇxᴇᴄᴜᴛᴇᴅ sɪʟᴇɴᴛʟʏ.")
