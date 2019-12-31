# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from telethon import events


@register(events.NewMessage(pattern=r"^.all", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    await event.delete()
    mentions = "@all"
    chat = await event.get_input_chat()
    async with event.iter_participants(chat, 100):
        mentions += f"[\u2063](tg://user?id={x.id})"
    await event.send_message(
        chat, mentions, reply_to=event.message.reply_to_msg_id)
