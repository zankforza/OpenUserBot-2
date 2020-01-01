# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from userbot.events import register


@register(pattern="^.tagall", outgoing=True)
async def tagall(event):
    if event.fwd_from:
        return
    mentions = "Bhai log"
    chat = await event.get_input_chat()
    async for x in events.iter_participants(chat, 100):
        mentions += f" \n [{x.first_name}](tg://user?id={x.id})"
    await event.reply(mentions)
    await event.delete()


@register(pattern="^.admin", outgoing=True)
async def admin(event):
    if event.fwd_from:
        return
    mentions = "bhai log : "
    chat = await event.get_input_chat()
    async for x in events.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f" \n [{x.first_name}](tg://user?id={x.id})"
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()

