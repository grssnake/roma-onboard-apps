#!/bin/sh

export DISPLAY=:0
chromium-browser --kiosk --disable-session-crashed-bubble --disable-infobars --disable-restore-session-state https://meet.jit.si/RobotRomaClass
