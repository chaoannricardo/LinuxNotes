#!/bin/bash

systemctl stop GuestMount.service
systemctl disable GuestMount.service
rm /etc/systemd/system/GuestMount.service
rm /etc/systemd/system/GuestMount.service # and symlinks that might be related
rm /usr/lib/systemd/system/GuestMount.service
rm /usr/lib/systemd/system/GuestMount.service # and symlinks that might be related
systemctl daemon-reload
systemctl reset-failed
