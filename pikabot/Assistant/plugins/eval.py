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

from Asst_modules import _eval
from pikabot.utils import pikatgbot

@ItzSjDude(pika=True, pattern="eval")
@pikatgbot('Owner')
async def _(event):
  await _eval(event)
