#!/bin/sh

cmd_start="/tmp/j.start"
cmd_stop="/tmp/j.stop"

if [ -f "$cmd_start" ]
then
    export DISPLAY=:0
	echo "$cmd_start found. Start jitsu"
    rm -rf "$cmd_start"
    chromium-browser --kiosk --disable-session-crashed-bubble --disable-infobars --disable-restore-session-state https://meet.jit.si/RobotRomaClass
fi

if [ -f "$cmd_stop" ]
then
	echo "$cmd_stop found. Stop jitsu"
    rm -rf "$cmd_stop"
    pkill -f -9 chromium
else
	echo "Nothing."
fi



