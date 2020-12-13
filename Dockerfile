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

RUN rm /var/lib/apt/lists/lock && rm /var/cache/apt/archives/lock && rm /var/lib/dpkg/lock* && apt-get update && apt-get install sudo -y && useradd -rm -d /home/itzsjdude -s /bin/bash -g root -G sudo -u 1001 itzsjdude
USER itzsjdude
WORKDIR /home/itzsjdude
RUN /tmp/pika.sh && chmod +x /usr/local/bin/* 
