#!/bin/bash

# Refernce: https://linuxconfig.org/how-to-run-script-on-startup-on-ubuntu-20-04-focal-fossa-server-desktop

# reference link for guest mount vhdx:
# https://www.nicholasmelnick.com/2020/07/sharing-your-wsl2-environment-with-linux/
# service stored place: /etc/systemd/system/
sudo guestmount -o allow_other \
  --add /media/storage/WSL_Storage/ext4.vhdx \
  -i ./wsl

echo > /home/ricardo/.guestmount_successfully
date >> /home/ricardo/.guestmount_successfully

# exit script with return code.
exit 0
