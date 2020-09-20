#!/bin/bash
sudo apt update
sudo apt install -y git
git clone https://github.com/SIT-DigiCre/serverside-primer.git ~/serverside-primer
cd ~/serverside-primer
./envinstall.sh

# install Python packages
sudo pip3 install pipenv flask
cd ~/serverside-primer/python
sudo pipenv install --system
cd ~/serverside-primer

# install Nodejs packages
cd ~/serverside-primer/nodejs
npm install
cd ~/serverside-primer
