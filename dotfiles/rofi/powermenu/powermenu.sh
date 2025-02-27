#!/bin/bash

# options to be displayed
option1=""
option2=""
option3=""
option4=""

# options passed into variable
options="$option1\n$option2\n$option3\n$option4"

chosen="$(echo -e "$options" | rofi -theme $HOME/.config/rofi/powermenu/config.rasi -lines 4 -dmenu -p "power" )"
case $chosen in
    $option1)
        bspc quit;;
    $option2)
        bspc wm -r;;
    $option3)
        reboot;;
    $option4)
	poweroff;;
esac