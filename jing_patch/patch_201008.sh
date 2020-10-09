#!/bin/bash

# Reference:
# https://askubuntu.com/questions/1279602/ubuntu-20-04-failed-to-set-moklistrt-invallid-parameter
sudo cp /boot/efi/EFI/ubuntu/grubx64.efi /boot/efi/EFI/ubuntu/shimx64.efi
sudo apt update
sudo apt upgrade -y
sudo apt autoremove -y

echo -e "\n\n\nThe patch has been executed successfully!\nReboot the computer in 5 seconds..."
sleep 5
reboot