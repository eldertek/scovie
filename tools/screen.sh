#!/bin/bash
xset s noblank &
xset s off &

# Store server_address in a variable
server_address="http://127.0.0.1"

# Make a boucle that will check if the server is up
while true; do
    # Check if the server is up
    if curl --output /dev/null --silent --head --fail "$server_address"; then
        # If the server is up, open the browser        
        unclutter &
        pkill chrome
        chromium-browser --kiosk --start-maximized "$server_address" --no-default-browser-check --noerrdialogs --no-message-box --disable-desktop-notifications --autoplay-policy=no-user-gesture-required --force-device-scale-factor=1.5
    else
        # If the server is down, wait 5 seconds and try again
        sleep 5
    fi
done
