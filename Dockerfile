#©ItzSjDude 
FROM ubuntu:20.04
COPY pika.sh /tmp/pika.sh
WORKDIR root/ItzSjDude
RUN /tmp/pika.sh && chmod +x /usr/local/bin/* 
