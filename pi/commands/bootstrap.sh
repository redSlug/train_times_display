#!/bin/bash

apt-get update
apt-get install -y git python3-pip

REPO_DIR=/home/pi/train_display
VENV_PATH="${REPO_DIR}/venv/bin/activate"


mkdir -p $REPO_DIR
git clone https://github.com/redSlug/train_display.git $REPO_DIR

cd $REPO_DIR

python3 -m virtualenv venv
source $VENV_PATH
pip3 install -r requirements.txt

make -C rpi-rgb-led-matrix/examples-api-use
