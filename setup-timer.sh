#!/bin/bash

WD=`pwd`
echo ${WD}
PYTHON_SCRIPT=`which python3`\ ${WD}/downloader.py

echo ${PYTHON_SCRIPT}

sed -e "s^<CMD>^ExecStart=`echo ${PYTHON_SCRIPT}`^g" downloader.service-config > downloader.service


mkdir -p ~/.config/systemd/user
cp downloader.service ~/.config/systemd/user/downloader.service
cp downloader.timer ~/.config/systemd/user/downloader.timer

systemctl --user daemon-reload 
systemctl --user enable downloader.service
systemctl --user enable downloader.timer
systemctl --user start downloader.timer
systemctl --user list-timers --all
