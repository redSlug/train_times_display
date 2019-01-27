#!/bin/bash

sudo apt-get update
sudo apt-get install -y git python3-pip
sudo apt-get install silversearcher-ag emacs

REPO_DIR=/home/pi/train_display
VENV_PATH="${REPO_DIR}/venv/bin/activate"
APP_DIR="${REPO_DIR}/pi"



mkdir -p $REPO_DIR

git clone --recurse-submodules -j8 git@github.com:redSlug/train_times_display.git $REPO_DIR

cd $REPO_DIR

sudo pip3 install virtualenv
python3 -m virtualenv venv
source $VENV_PATH
pip3 install -r requirements.txt

cd $APP_DIR

make -C rpi-rgb-led-matrix/examples-api-use

mkdir -p "${APP_DIR}/generated"
