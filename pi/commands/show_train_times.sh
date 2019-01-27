#!/bin/bash

# crontab
# @reboot /home/pi/train_display/pi/commands/show_train_times.sh >> /home/pi/train_display/log


source /home/pi/train_display/pi/commands/env_vars


get_train_data() {
    source $VENV_PATH
    python app.py
}

cleanup() {
    echo "Cleaning stuff up" >> log
    sudo pkill demo
    exit
}


main () {
    pushd $APP_DIR

    if [ ! -f $IMG_PATH ]; then
        echo "File not found!" >> log
        exit 1
    fi

    trap cleanup EXIT
    while true; do
        get_train_data
        source env_vars
        sudo pkill demo
        sudo rpi-rgb-led-matrix/examples-api-use/demo -D 1 $IMG_PATH --led-no-hardware-pulse --led-rows=16 --led-cols=32 -m $delay_milliseconds --led-daemon --led-brightness=10
        sleep $sleep_seconds
    done

    popd
}

main
