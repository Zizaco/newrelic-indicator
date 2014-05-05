#!/bin/bash

while true; do
    read -p "Do you wish to run Newrelic Indicator at startup? [yn] " yn
    case $yn in
        [Yy]* )
            DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
            DESKTOP_FILE="/etc/xdg/autostart/indicator-newrelic.desktop"
            sudo touch $DESKTOP_FILE
            sudo chmod 777 $DESKTOP_FILE
            sudo echo "[Desktop Entry]" > $DESKTOP_FILE
            sudo echo "Type=Application" >> $DESKTOP_FILE
            sudo echo "Exec=$DIR/main.py" >> $DESKTOP_FILE
            sudo echo "Hidden=false" >> $DESKTOP_FILE
            sudo echo "NoDisplay=false" >> $DESKTOP_FILE
            sudo echo "X-GNOME-Autostart-enabled=true" >> $DESKTOP_FILE
            sudo echo "Name=Newrelic Indicator" >> $DESKTOP_FILE
            sudo echo "Comment=Indicator to monitor metrics from newrelic for Unity" >> $DESKTOP_FILE
            sudo chmod 644 $DESKTOP_FILE
            echo "..."
            echo "Added Newrelic Indicator to system startup"
            break;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.";;
    esac
done


