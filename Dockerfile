FROM ubuntu:focal

EXPOSE 22 80 8800

ENV TZ=Asia/Tokyo
ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y tzdata && apt install -y sudo git
RUN echo "user ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

RUN useradd -m -U -s /bin/bash user
RUN echo "password\npassword" | passwd user
USER user
WORKDIR /home/user

COPY . /home/user/serverside-primer

RUN cd ~/serverside-primer && \
    ./installscript.sh

CMD sudo service ssh start && sudo service apache2 start && /bin/bash
