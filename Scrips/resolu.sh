#!/bin/bash


export DISPLAY=:0
echo "eDP-1 Current resolution:"
xrandr | grep "1280x800      60.00"
sleep 20
xrandr --newmode "840x525R"   32.25  840 888 920 1000  525 528 538 544 +hsync -vsync
xrandr --addmode eDP-1 "840x525R"
xrandr --output eDP-1 --mode "840x525R"
open
