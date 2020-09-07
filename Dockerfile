FROM ubuntu:latest
ENV TZ=Asia/Kolkata
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN echo -e "\nexport TERM=xterm" >> ~/.bashrc
RUN apt-get update && apt upgrade -y

RUN apt-get install -y\
    coreutils \
    bash \
    nodejs \
    bzip2 \
    curl \
    figlet \
    gcc \
    g++ \
    git \
    aria2 \
    util-linux \
    libevent-dev \
    libjpeg-dev \
    libffi-dev \
    libpq-dev \
    libwebp-dev \
    libxml2 \
    libxml2-dev \
    libxslt-dev \
    musl \
    neofetch \
    libcurl4-openssl-dev \
    postgresql \
    postgresql-client \
    postgresql-server-dev-all \
    openssl \
    pv \
    jq \
    wget \
    python3 \
    python3-dev \
    python3-pip \
    libreadline-dev \
    zipalign \
    sqlite \
    ffmpeg \
    libsqlite3-dev \
    sudo \
    zlib1g-dev \
    recoverjpeg \
    zip \
    megatools \
    libfreetype6-dev \
    procps \
    policykit-1


RUN aria2c https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && apt install -y ./google-chrome-stable_current_amd64.deb && rm -rf google-chrome-stable_current_amd64.deb
RUN git clone https://github.com/ItzSjDude/PikachuUserbot /root/ItzSjDude
RUN mkdir /root/ItzSjDude/bin/  && mkdir /root/ItzSjDude/plugins/ && mkdir root/ItzSjDude/pikabot/main_plugs/
WORKDIR /root/ItzSjDude
RUN pip3 install -r requirements.txt
CMD ["python3","-m","pikabot"]
