#!/bin/bash

# Install Yagmail for Python
sudo pip install yagmail[all]
sudo chmod +x /home/pi/ipcheck.py

# Write out current crontab
sudo crontab -l > mycron

# Echo new cron into cron file
echo "0 0 1 * * sudo python /home/pi/ipcheck.py" >> mycron

# Install new cron file
sudo crontab mycron
sudo rm mycron
