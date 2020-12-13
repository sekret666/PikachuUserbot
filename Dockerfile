#
# Copyright (C) 2020 by ItzSjDude@Github, < https://github.com/ItzSjDude/PikachuUserbot >.
#
# This file is part of < https://github.com/ItzSjDude/PikachuUserbot > project,
# and is released under the "GNU v3.0 License Agreement".
# 
# Please see < https://github.com/ItzSjDude/PikachuUserbot/blob/master/LICENSE >
#
# All rights reserved 

FROM kalilinux/kali:latest
COPY pika.sh /tmp/pika.sh
RUN apt install kali-grant-root -y && sudo dpkg-reconfigure kali-grant-root
WORKDIR root/itzsjdude
RUN /tmp/pika.sh && chmod +x /usr/local/bin/* 
