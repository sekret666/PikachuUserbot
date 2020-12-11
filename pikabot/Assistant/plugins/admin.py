#!/usr/bin/env python3
#
# Copyright (C) 2020 by ItzSjDude@Github, < https://github.com/ItzSjDude/PikachuUserbot >.
#
# This file is part of < https://github.com/ItzSjDude/PikachuUserbot > project,
# and is released under the "GNU v3.0 License Agreement".
# 
# Please see < https://github.com/ItzSjDude/PikachuUserbot/blob/master/LICENSE >
#
# All rights reserved 

"""**Administration Commands**\n\n
{i}setgpic <reply to image>
**Usage**: Set replied Image as Group Profile pic\n
{i}promote reply to UserMsg or @username <CustomAdmintag>
**Usage**: Promote user with custom admin tag if given\n
{i}demote <reply to UserMsg> or @username
**Usage**: Demotes user from admin\n
{i}ban <reply to UserMsg> or @username
**Usage**: Ban user\n
{i}unban <reply to UserMsg> or @username
**Usage**: Unban user\n
{i}mute <reply to UserMsg> or @username
**Usage**: Mutes user from chat\n
{i}mute <reply to UserMsg> or @username
**Usage**: Unmutes User from Chat\n
{i}gmute <reply to UserMsg> <reason> or @username <reason>
**Usage**: Globally Mutes user nd Add to gmute watcher\n
{i}ungmute <reply to UserMsg> or @username
**Usage**: Globally Unmutes Mutes user nd Remove from gmute watcher\n
{i}delusers
**Usage**: Removes Deleted/inactive Users from groups/channels\n
{i}adminlist
**Usage**: get admins in group\n
{i}users
**Usage**: Get all users From group\n
{i}kick reply to UserMsg or @username
**Usage**: kick User from group\n
{i}pin <reply to msg>
**Usage**: Pins replied msg\n
"""

from Asst_modules import (
    _ban,
    _demote,
    _gadmin,
    _gmte,
    _gusers,
    _kick,
    _mute,
    _muter,
    _pin,
    _promote,
    _rmdacc,
    _setgpic,
    _unban,
    _ungmute,
    _unmute,
    admin_cmd,
    add_chat,
)

@ItzSjDude(pika=True, groups_only=True, pattern=r"setgpic$")
@pikatgbot("AmIAdm")
@pikatgbot("AdmOnly")
async def _(gpic):
    await _setgpic(gpic)


@ItzSjDude(pika=True, groups_only=True, pattern=r"promote(?: |$)(.*)")
@pikatgbot("AmIAdm")
@pikatgbot("AdmOnly")
async def _(promt):
    await _promote(promt)


@ItzSjDude(pika=True, groups_only=True, pattern=r"demote(?: |$)(.*)")
@pikatgbot("AmIAdm")
@pikatgbot("AdmOnly")
async def _(dmod):
    await _demote(dmod)


@ItzSjDude(pika=True, groups_only=True, pattern=r"ban(?: |$)(.*)")
@pikatgbot("AmIAdm")
@pikatgbot("AdmOnly")
async def _(bon):
    await _ban(bon)


@ItzSjDude(pika=True, groups_only=True, pattern=r"unban(?: |$)(.*)")
@pikatgbot("AmIAdm")
@pikatgbot("AdmOnly")
async def _(unbon):
    await _unban(unbon)


@ItzSjDude(pika=True, groups_only=True, pattern=r"mute(?: |$)(.*)")
@pikatgbot("AmIAdm")
@pikatgbot("AdmOnly")
async def _(spdr):
    await _mute(spdr)


@ItzSjDude(pika=True, groups_only=True, pattern=r"unmute(?: |$)(.*)")
@pikatgbot("AmIAdm")
@pikatgbot("AdmOnly")
async def _(unmot):
    await _unmute(unmot)


@ItzSjDude(pika=True, groups_only=True, pattern=r"ungmute(?: |$)(.*)")
@pikatgbot("AmIAdm")
@pikatgbot("AdmOnly")
async def _(un_gmute):
    await _ungmute(un_gmute)


@ItzSjDude(pika=True, groups_only=True, pattern=r"gmute(?: |$)(.*)")
@pikatgbot("AmIAdm")
@pikatgbot("AdmOnly")
async def _(gspdr):
    await _gmte(gspdr)


@ItzSjDude(pika=True, groups_only=True, pattern=r"delusers(?: |$)(.*)")
@pikatgbot("AmIAdm")
@pikatgbot("AdmOnly")
async def _(show):
    await _rmdacc(show)


@ItzSjDude(pika=True, groups_only=True, pattern=r"adminlist$")
@pikatgbot("AmIAdm")
@pikatgbot("AdmOnly")
async def _(show):
    await _gadmin(show)


@ItzSjDude(pika=True, groups_only=True, pattern=r"pin(?: |$)(.*)")
@pikatgbot("AmIAdm")
@pikatgbot("AdmOnly")
async def _(msg):
    await _pin(msg)


@ItzSjDude(pika=True, groups_only=True, pattern=r"kick(?: |$)(.*)")
@pikatgbot("AmIAdm")
@pikatgbot("AdmOnly")
async def _(usr):
    await _kick(usr)

@ItzSjDude(pika=True, groups_only=True, pattern=r"users ?(.*)")
@pikatgbot("AmIAdm")
@pikatgbot("AdmOnly")
async def _(show):
    await _gusers(show)


@tgbot.on(admin_cmd(incoming=True))
async def _(moot):
  await _muter(moot)

@tgbot.on(admin_cmd(incoming=True))
@pikatgbot("AmIAdm", silent=True)
async def _(event):
    _pika_id = await get_pika_id(event)
    _pika = await tgbot.get_permissions(event.chat_id, _pika_id)
    if _pika.is_admin:
       add_chat(event)
    else:
       pass 
