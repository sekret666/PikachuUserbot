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

from Asst_modules import _add_notes, _allnotes, _remove_notes, admin_cmd, note_incm, tgbot


@ItzSjDude(pika=True, groups_only=True, pattern="^/notes$")
async def _(event):
    await _allnotes(event)


@ItzSjDude(pika=True, groups_only=True, pattern=r"save (\w*)")
@pikatgbot("AmIAdm")
@pikatgbot("AdmOnly")
async def _(event):
    await _add_notes(event)


@ItzSjDude(pika=True, pattern=r"clear (\w*)")
@pikatgbot("AmIAdm")
@pikatgbot("AdmOnly")
async def _(event):
    await _remove_notes(event)


@tgbot.on(admin_cmd(pattern=r"\#\w*", incoming=True))
async def _(getnt):
    if not getnt.is_private:
       await note_incm(getnt)
    else:
      return 
