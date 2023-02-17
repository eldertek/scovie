#!/bin/bash
xset s noblank &
xset s off &
unclutter &
pkill chrome
/usr/bin/google-chrome --kiosk --start-maximized "http://127.0.0.1" --no-default-browser-check --noerrdialogs --no-message-box --disable-desktop-notifications --autoplay-policy=no-user-gesture-required --force-device-scale-factor=1.5