# MTA Train Times Display

Displays upcoming train information in minutes to a 32x16 RGB LED Grid

## Setup
- get a free [MTA developer's API key](https://datamine.mta.info/user/register)
- add network name and password to `recipe.xml` between the `**` symbols, removing the `**` symbols
- flash SD card to full raspian using [PiBakery](http://www.pibakery.org/download.html) and `recipe.xml` 
- make sure the Pi has an uninterrupted power supply the first time it boots up, so it can install and set up everything it needs to, then you can `ssh pi@trainpi.local`, password will be `goodtimes` unless you change it
- connect the pi to the MPC1073, connect the MPC1073 to the HUB75 LED matrix

### Cron
- schedule [cronjob](https://www.raspberrypi.org/documentation/linux/usage/cron.md) to get train schedule every 30 seconds, and render upon boot

## BOM
- Raspberry Pi or [Pi Zero](https://www.adafruit.com/product/3708) with [Hammer Header Male Connector](https://www.adafruit.com/product/3662), and [power supply](https://www.adafruit.com/product/1995)
- [MPC1073](http://www.electrodragon.com/product/rgb-matrix-panel-drive-board-raspberry-pi/) and CR1220 battery
- 16+ GB SD card, and card reader / writer
- [32x16 LED matrix](https://www.adafruit.com/product/420) with ribbon and 5 Volt 2 Amp power supply
- [Female DC Power adapter - 2.1mm jack to screw terminal block](https://www.adafruit.com/product/368) to go in back of the LED Matrix

## Troubleshooting
- wait at least 2 minutes after powering your pi with the LED display for the train times to appear
- after plugging in a pi with a freshly baked flash card, wait at least 5 minutes
- to see if program that renders the train times to LED display is running, `ps aux | grep demo`

## Thank You
- [Henner Zeller for sharing your LED Matrix code](https://github.com/hzeller/rpi-rgb-led-matrix)
