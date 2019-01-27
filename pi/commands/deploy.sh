#!/bin/bash

source env_vars
cd $REPO_DIR
git pull

source $VENV_PATH
pip3 install -r requirements.txt
