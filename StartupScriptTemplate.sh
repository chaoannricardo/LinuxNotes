#!/bin/bash -e

# The script needs to be stored inside /etc/rc.local

# reference link for gust mount vhdx:
# https://www.nicholasmelnick.com/2020/07/sharing-your-wsl2-environment-with-linux/
sudo guestmount -o allow_other \
  --add /media/storage/WSL_Storage/ext4.vhdx \
  -i ./wsl

# exit script with return code.
exit 0