#!/bin/bash
#
# Copyright (C) 2020 by ItzSjDude@Github, < https://github.com/ItzSjDude/PikachuUserbot >.
#
# This file is part of < https://github.com/ItzSjDude/PikachuUserbot > project,
# and is released under the "GNU v3.0 License Agreement".
# 
# Please see < https://github.com/ItzSjDude/PikachuUserbot/blob/master/LICENSE >
#
# All rights reserved 

_logo() {
    echo '
    ╔═╦╦╗───╔╗──╔╗
    ║╬╠╣╠╦═╗║╚╦═╣╚╗
    ║╔╣║═╣╬╚╣╬║╬║╔╣
    ╚╝╚╩╩╩══╩═╩═╩═╝
    '
}

_cleanup() {
    echo 'Cleaning up Pikabot'
    rm -rf ./* && rm -rf ./.gitignore && rm -rf ./.git
} 

_source() {
    echo 'Getting Source Ready' 
    git clone -b Beta https://github.com/ItzSjDude/PikachuUserbot ./
}

_upgradePip() {
    echo '••• Updating Pip •••' 
    pip3 install -U pip &> /dev/null
    echo '••• Updated Pip •••'
}

_insReq() {
    echo '••• Installing Requirements •••'
    pip install -r requirements.txt &> /dev/null
    echo '••• Installed Requirements •••'
}

start() {
    _logo
    _cleanup
    _source
    _upgradePip
    _insReq
    mkdir ./pikabot/main_plugs
    python3 -m pikabot
}
