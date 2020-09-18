#!/bin/bash
sudo apt update
sudo apt install -y vim emacs curl ssh
sudo apt install -y php python3 python3-pip nodejs npm golang

# install VSCode
if [ -n "$GUI" ]; then
    curl -L -o code.deb "https://go.microsoft.com/fwlink/?LinkID=760868"
    sudo apt install -y ./code.deb
    rm code.deb
fi
