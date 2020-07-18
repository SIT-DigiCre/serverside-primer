#!/bin/bash
sudo apt update
sudo apt install -y vim emacs curl ssh
sudo apt install -y php python3 python3-pip nodejs npm golang

# install Python packages
sudo pip3 install pipenv flask
cd ~/serverside-primer/python
sudo pipenv install --system
cd ~/serverside-primer

# install Nodejs packages
cd ~/serverside-primer/nodejs
npm install
cd ~/serverside-primer

# install VSCode
if [ -n "$GUI" ]; then
    curl -L -o code.deb "https://go.microsoft.com/fwlink/?LinkID=760868"
    sudo apt install -y ./code.deb
    rm code.deb
fi
