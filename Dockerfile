#©ItzSjDude 

FROM ubuntu:latest
COPY pika.sh /tmp/pika.sh
WORKDIR root/ItzSjDude
RUN /tmp/start.sh && chmod +x /usr/local/bin/* 
