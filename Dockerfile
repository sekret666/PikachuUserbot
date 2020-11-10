#©ItzSjDude 
FROM kalilinux/kali-rolling
COPY pika.sh /tmp/pika.sh
WORKDIR root/ItzSjDude
RUN /tmp/pika.sh && chmod +x /usr/local/bin/* 
