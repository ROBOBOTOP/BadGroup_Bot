from pyrogram import filters
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, Message

from BADMUNDA import LOGGER
from BADMUNDA.bot_class import BAD
from BADMUNDA.database.rules_db import Rules
from BADMUNDA.utils.custom_filters import admin_filter, command
from BADMUNDA.utils.kbhelpers import ikb
from BADMUNDA.utils.string import build_keyboard, parse_button
from BADMUNDA.vars import Config


@BAD.on_message(command("rules") & filters.group)
async def get_rules(_, m: Message):
    db = Rules(m.chat.id)
    msg_id = m.reply_to_message.id if m.reply_to_message else m.id

    rules = db.get_rules()
    LOGGER.info(f"{m.from_user.id} fetched rules in {m.chat.id}")
    if m and not m.from_user:
        return

    if not rules:
        await m.reply_text(
            text="The Admins for this group have not setup rules! That doesn't mean you can break the DECORUM of this group !",
            quote=True,
        )
        return

    priv_rules_status = db.get_privrules()

    if priv_rules_status:
        pm_kb = ikb(
            [
                [
                    (
                        "Rules",
                        f"https://t.me/{Config.BOT_USERNAME}?start=rules_{m.chat.id}",
                        "url",
                    ),
                ],
            ],
        )
        await m.reply_text(
            text="Click on the below button to see this group rules!",
            quote=True,
            reply_markup=pm_kb,
            reply_to_message_id=msg_id,
        )
        return

    formated = rules
    teks, button = await parse_button(formated)
    button = await build_keyboard(button)
    button = ikb(button) if button else None
    textt = teks
    await m.reply_text(
        text=f"""The rules for <b>{m.chat.title} are:</b>
{textt}""",
        disable_web_page_preview=True,
        reply_to_message_id=msg_id,
        reply_markup=button
    )
    return


@BAD.on_message(command("setrules") & admin_filter)
async def set_rules(_, m: Message):
    db = Rules(m.chat.id)
    if m and not m.from_user:
        return

    if m.reply_to_message and m.reply_to_message.text:
        rules = m.reply_to_message.text.markdown
    elif (not m.reply_to_message) and len(m.text.split()) >= 2:
        rules = m.text.split(None, 1)[1]
    else:
        return await m.reply_text("Provide some text to set as rules !!")

    if len(rules) > 4000:
        rules = rules[0:3949]  # Split Rules if len > 4000 chars
        await m.reply_text("Rules are truncated to 3950 characters!")

    db.set_rules(rules)
    LOGGER.info(f"{m.from_user.id} set rules in {m.chat.id}")
    await m.reply_text(text="Successfully set rules for this group.")
    return


@BAD.on_message(
    command(["pmrules", "privaterules"]) & admin_filter,
)
async def priv_rules(_, m: Message):
    db = Rules(m.chat.id)
    if m and not m.from_user:
        return

    if len(m.text.split()) == 2:
        option = (m.text.split())[1]
        if option in ("on", "yes"):
            db.set_privrules(True)
            LOGGER.info(f"{m.from_user.id} enabled privaterules in {m.chat.id}")
            msg = f"Private Rules have been turned <b>on</b> for chat <b>{m.chat.title}</b>"
        elif option in ("off", "no"):
            db.set_privrules(False)
            LOGGER.info(f"{m.from_user.id} disbaled privaterules in {m.chat.id}")
            msg = f"Private Rules have been turned <b>off</b> for chat <b>{m.chat.title}</b>"
        else:
            msg = "Option not valid, choose from <code>on</code>, <code>yes</code>, <code>off</code>, <code>no</code>"
        await m.reply_text(msg)
    elif len(m.text.split()) == 1:
        curr_pref = db.get_privrules()
        msg = (
            f"Current Preference for Private rules in this chat is: <b>{curr_pref}</b>"
        )
        LOGGER.info(f"{m.from_user.id} fetched privaterules preference in {m.chat.id}")
        await m.reply_text(msg)
    else:
        await m.reply_text(text="Please check help on how to use this this command.")

    return


@BAD.on_message(command("clearrules") & admin_filter)
async def clear_rules(_, m: Message):
    db = Rules(m.chat.id)
    if m and not m.from_user:
        return

    rules = db.get_rules()
    if not rules:
        await m.reply_text(
            text="The Admins for this group have not setup rules! That doesn't mean you can break the DECORUM of this group !"
        )
        return

    await m.reply_text(
        text="Are you sure you want to clear rules?",
        reply_markup=ikb(
            [[("⚠️ Confirm", "clear_rules"), ("❌ Cancel", "close_admin")]],
        ),
    )
    return


@BAD.on_callback_query(filters.regex("^clear_rules$"))
async def clearrules_callback(_, q: CallbackQuery):
    Rules(q.message.chat.id).clear_rules()
    await q.message.edit_text(text="Successfully cleared rules for this group!")
    LOGGER.info(f"{q.from_user.id} cleared rules in {q.message.chat.id}")
    await q.answer("Rules for the chat have been cleared!", show_alert=True)
    return


__PLUGIN__ = "Rᴜʟᴇs"

__alt_name__ = ["rule"]

__HELP__ = """
**Rᴜʟᴇs**

Sᴇᴛ ʀᴜʟᴇs ғᴏʀ ʏᴏᴜ ᴄʜᴀᴛ sᴏ ᴛʜᴀᴛ ᴍᴇᴍʙᴇʀs ᴋɴᴏᴡ ᴡʜᴀᴛ ᴛᴏ ᴅᴏ ᴀɴᴅ ᴡʜᴀᴛ ɴᴏᴛ ᴛᴏ ᴅᴏ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ!

• /ʀᴜʟᴇs: ɢᴇᴛ ᴛʜᴇ ʀᴜʟᴇs ғᴏʀ ᴄᴜʀʀᴇɴᴛ ᴄʜᴀᴛ.

Aᴅᴍɪɴ ᴏɴʟʏ:
• /sᴇᴛʀᴜʟᴇs <ʀᴜʟᴇs>: Sᴇᴛ ᴛʜᴇ ʀᴜʟᴇs ғᴏʀ ᴛʜɪs ᴄʜᴀᴛ, ᴀʟsᴏ ᴡᴏʀᴋs ᴀs ᴀ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ.
• /ᴄʟᴇᴀʀʀᴜʟᴇs: Cʟᴇᴀʀ ᴛʜᴇ ʀᴜʟᴇs ғᴏʀ ᴛʜɪs ᴄʜᴀᴛ.
• /ᴘʀɪᴠʀᴜʟᴇs <ᴏɴ/ʏᴇs/ɴᴏ/ᴏғғ>: Tᴜʀɴs ᴏɴ/ᴏғғ ᴛʜᴇ ᴏᴘᴛɪᴏɴ ᴛᴏ sᴇɴᴅ ᴛʜᴇ ʀᴜʟᴇs ᴛᴏ PM ᴏғ ᴜsᴇʀ ᴏʀ ɢʀᴏᴜᴘ.

Nᴏᴛᴇ Fᴏʀᴍᴀᴛ
    Cʜᴇᴄᴋ /ᴍᴀʀᴋᴅᴏᴡɴʜᴇʟᴘ ғᴏʀ ʜᴇʟᴘ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ ғᴏʀᴍᴀᴛᴛɪɴɢ!
"""